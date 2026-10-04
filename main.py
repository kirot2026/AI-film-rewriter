from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from openai import OpenAI
import json
load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")
if not api_key:
    raise ValueError("DASHSCOPE_API_KEY 未配置")
client = OpenAI(api_key=api_key,
                base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")

app = FastAPI()
class RewriteRequest(BaseModel):
    film_name: str
    background:str
    ori_ending:str
    change_point: str
    ending_type: str

def generate_ending(film_name:str,background:str,ori_ending:str,change_point:str,ending_type:str):
    response = client.chat.completions.create(
    model="qwen-flash",  
    messages=[{"role": "user", 
               "content": (f"""你是一名电影编剧。请根据以下信息从【剧情改变点】开始改变故事,重新设计故事结局.
                                     【电影/故事名称】{film_name}
                                     【故事背景】{background}
                                     【原始结局】{ori_ending}
                                     【剧情改变点】{change_point}
                                     【目标结局类型】{ending_type}
                                     【字段】{{"ending_type": "用户选择的目标结局类型","new_ending": "...","key_changes": ["...","..."]}}
                                     【要求】1.只返回一个JSON对象。不要任何解释文字。不要用 ```json 包裹。第一个字符必须是 {{，最后一个字符必须是 }}。JSON中每个列表元素之间必须有逗号，多个键值对之间也必须有逗号。
                                     2. 保留原作主要人物关系和世界观
                                     3. 不直接复制原作台词
                                     4. 不完全推翻前面的故事
                                     5. 新结局必须由剧情改变点自然发展出来
                                     6. 保持人物行为符合人物设定
                                     7.new_ending五百字以内,每条key_changes不超过25字"""
                                     )}])
    text=response.choices[0].message.content
    try:
        result=json.loads(text)
        return result
    except json.JSONDecodeError:
        raise ValueError("模型返回的不是合法JSON")

@app.post("/rewriter")
def rewrite(request: RewriteRequest):
    try:
        result = generate_ending(request.film_name,request.background,request.ori_ending,request.change_point,request.ending_type)
        return result
    except ValueError as e:
        raise HTTPException(status_code=500,detail=str(e))
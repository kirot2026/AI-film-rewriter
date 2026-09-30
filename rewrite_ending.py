import os
from dotenv import load_dotenv
from openai import OpenAI
import json
load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")
client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
film_name=input("请输入要改编的电影名：")
background=input("请输入故事背景：")
ori_ending=input("请输入电影原始结局：")
change_point=input("请输入剧情改变点：")
ending_type=input("请输入希望的结局类型1.Happy Ending2.Bad Ending3.Open Ending4.Bittersweet Ending：")

response = client.chat.completions.create(
    model="qwen-flash",  
    messages=[
        {"role": "user", "content": (f"""你是一名电影编剧。请根据以下信息从【剧情改变点】开始改变故事,重新设计故事结局.
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
print(text)
result=json.loads(text)
print(f"改编{result['ending_type']}:{result['new_ending']}")
print("关键变更：")
for changes in result["key_changes"]:
    print(changes)

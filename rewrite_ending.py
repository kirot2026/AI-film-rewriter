import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")
client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
film_name=input("请输入要改编的电影名：")
background=input("请输入故事背景：")
ori_ending=input("请输入电影原始结局：")
ending_type=input("请选择希望的结局类型1.Happy Ending2.Bad Ending3.Open Ending4.Bittersweet Ending：")

response = client.chat.completions.create(
    model="qwen-flash",  
    messages=[
        {"role": "user", "content": (f"""你是一名电影编剧。请根据以下信息重新设计故事结局.
                                     【电影/故事名称】{film_name}
                                     【故事背景】{background}
                                     【原始结局】{ori_ending}
                                     【目标结局类型】{ending_type}
                                     【要求】1.保留主要人物和故事背景2.不要完全推翻前面的故事3.通过合理的剧情变化实现新的结局4.五百字以内"""
                                     )}])
text=response.choices[0].message.content
print(text)

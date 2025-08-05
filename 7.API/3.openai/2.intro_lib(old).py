# pip install openai==0.3 보다 작은 버전.. 
# pip install openai==0.28

import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = openai_api_key

# 아래 openai.ChatCompletion 이라고 출발하는 사이트는 일단 보지말고 닫을것.
# 매우 구버전API 임으로.. 지금은 동작하지 않음. (openai==0.3.0 이전의 문법임)
response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages = [
        {'role':'user', 'content': '아무말이나 적어봅시다.'}
    ]
)

print(response['choices'][0]['message']['content'])

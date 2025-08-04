import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=openai_api_key)

# client.chat.completion 으로 시작하는게 0.3 이후의 버전 문법임
response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages = [
        {'role':'user', 'content': '아무말이나 적어봅시다.'}
    ]
)

print(response.choices[0].message.content)

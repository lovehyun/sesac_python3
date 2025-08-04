from dotenv import load_dotenv
import os
import requests

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

response = requests.post('https://api.openai.com/v1/chat/completions',
    json={
        'model':'gpt-4o',
        'messages': [
            # {"role":"user", "content": "잠자리에 들기 전에 양에 대한 스토리를 한문장 말해주시오."}
            {"role":"user", "content": "어떤 옵션이 있다고?? 다시 말해줘"}
        ]
    },
    headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}',
    }
)

response_data = response.json()
print(response_data['choices'][0]['message']['content'])

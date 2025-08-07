import os
import json
from dotenv import load_dotenv

from openai import OpenAI

from services import todo_service as todo

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise RuntimeError("API키가 없습니다!!")

client = OpenAI(api_key=API_KEY)

def ask_gpt(question):
    my_todo_list = todo.get_all()
    
    system_prompt1 = f"""
당신은 사용자의 TODO 리스트를 관리해주는 비서입니다. 
사용자의 TODO 항목과 질문에 대해서 간결하게 답변해 주세요.

[할 일 목록]
{my_todo_list}
"""  

    system_prompt2 = f"""
당신은 사용자의 TODO 리스트를 관리해주는 비서입니다. 
당신은 사용자의 질문에 대해서 아래 중에 하나를 골라서 action 을 선택하고 답변해야 합니다.
사용자의 TODO 항목과 질문에 대해서 간결하게 답변해 주세요.

[출력 형식]
{{ "action": "add", "item": [항목] }} - 할일을 추가해야 할 때
{{ "action": "delete", "item": [항목] }} - 할일을 안할꺼거나, 잘못 추가했을때
{{ "action": "update", "item": [항목] }} - 할일을 다했거나, 다한일을 다시 해야 할 때
{{ "action": "list" }} - 할일을 보여줘야 할 때
{{ "action": "nothing }} - 어떻게 판단해야할지 모를때 또는 TODO 리스트와는 쓸대없는 질문이 들어왔을때

[할 일 목록]
{my_todo_list}
"""  

    system_prompt = system_prompt2
    print("내가 GPT에게 할 질문:\n", system_prompt)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content": system_prompt},
            {"role":"user", "content": question}
        ]
    )
    
    reply = response.choices[0].message.content.strip()
    
    my_action = json.loads(reply)
    if my_action['action'] == 'add':
        print("추가할 코드 짜기")
        reply = "점심먹고 짤꺼라고 말하기"
    elif my_action['action'] == 'delete':
        print("삭제할 코드 짜기")
        reply = "점심먹고 짤꺼라고 말하기"
    elif my_action['action'] == 'list':
        print("삭제할 코드 짜기")
        reply = "점심먹고 짤꺼라고 말하기"
    elif my_action['action'] == 'update':
        print("삭제할 코드 짜기")
        reply = "점심먹고 짤꺼라고 말하기"
    else:
        print("아무것도 안하기")
        reply = "사용자에게 올바른 입력하라고 말하기"
    
    return reply


from dotenv import load_dotenv

from langchain_openai import OpenAI  # Completion 모델
from langchain_openai import ChatOpenAI  # Chat 모델 (QA모델)

load_dotenv()

print('----- 1 -----')
llm = OpenAI(max_tokens=1000) # gpt-3.5-turbo-instruct  <- completion 모델
prompt = "인공지능이란"
result = llm.invoke(prompt)
print(result)

print('----- 2 -----')
llm2 = ChatOpenAI(model="gpt-3.5-turbo") # gpt-3.5-turbo <- chat 모델
prompt = "인공지능이란"
result = llm2.invoke(prompt)
print(result.content)

print('----- 3 -----')
from langchain.schema import SystemMessage, HumanMessage
# Chat 모델을 제대로 쓰려면... 이렇게 페르소나 설정 (SystemMessage) 및 역할 (HumanMessage, AIMessage) 등을 지정해서 Content 를 채우기

llm2 = ChatOpenAI(model="gpt-3.5-turbo") # gpt-3.5-turbo <- chat 모델
prompt = [
    SystemMessage(content="당신은 인공지능 분야의 전문가 입니다."),
    HumanMessage(content="인공지능이란")
]
result = llm2.invoke(prompt)
print(result.content)

print('----- 4 -----')
from langchain.schema import SystemMessage, HumanMessage, AIMessage

llm2 = ChatOpenAI(model="gpt-3.5-turbo") # gpt-3.5-turbo <- chat 모델
prompt = [
    SystemMessage(content="당신은 요리 레시피 연구가 입니다."),
    HumanMessage(content="디저트 케이크를 맛있게 만들려면"),
    AIMessage(content="신선한 재료를 사용하고, 정확한 계량과 온도 조절로 부드럽고 촉촉한 식감을 살리는 것이 비결입니다."),
    HumanMessage(content="식감을 살리는 비결은?"),
]
result = llm2.invoke(prompt)
print(result.content)

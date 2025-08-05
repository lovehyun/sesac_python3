from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

load_dotenv()

# 1. 템플릿 정의
template = "다음 수신자에게 주제의 내용에 해당하는 회사의 공식 이메일 형태로 작성해주세요.\n\n수신자: {recipient}\n\n주제: {topic}"
prompt = PromptTemplate(input_variables=["recipient", "topic"], template=template)

# 2. 모델 정의
llm = OpenAI(temperature=1.0, max_tokens=1000) # 창의력있게 생성할꺼니깐... 메일 본문이 길어질수 있으니깐... (기본값: max_tokens=256)

# 3. 체인 생성
chain = prompt | llm

# 4. 입력 및 호출
input_text = {
    # "recipient": "마케팅팀", "topic": "신제품 출시를 위한 전략"
    # "recipient": "인사팀", "topic": "버그를 많이 만드는 개발자 해고"
    "recipient": "CEO", "topic": "회사의 중요 인재인 개발자를 해고시킨 인사팀장 해고"
}

result = chain.invoke(input_text)
print("최종결과: ", result)

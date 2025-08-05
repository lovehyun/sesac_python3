from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


# 1. 프롬프트 생성기 생성
template = """You are a naming consultant. 
Suggest 5 creative company names for a {company} that makes {product}
"""

prompt = PromptTemplate(
    input_variables=['company', 'product'],
    template=template
)

# 2. 모델 생성
llm = OpenAI() # 필요시 모델, 키, 온도 등을 설정한다

# 3. 나의 커스텀 아웃풋 파서 정의
def my_function(output):
    print("\nRAW 출력값은:")
    print(output)
    cleaned_output = output.strip().replace('.', "") # 다양한 공백 제거하는...
    return {"final_response": cleaned_output}

# 4. 체인 만들기 = (prompt -> llm -> outputparser) 지금의 parser는 내가 정의할 Lambda임.
# 이 예시에서 정의한 lambda는?? {"response": result} 라는 형태로 담기 위한 커스텀 함수임.
# chain = prompt | llm | RunnableLambda(lambda x: {"response": x.strip()})
chain = prompt | llm | RunnableLambda(my_function)

# 5. 결과를 도출한다 (위의 생성기들을 연결한 체인(prompt -> llm -> output)을 실행한다.)
inputs = {'company': 'high-tech startup', 'product': 'mobile games'}

result = chain.invoke(inputs)

print(f"최종결과:\n{result}")

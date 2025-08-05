from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import CommaSeparatedListOutputParser

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

# 3. 출력 파서를 생성한다
parser = StrOutputParser()
parser_csv = CommaSeparatedListOutputParser()

# 4. 체인 만들기 = LCEL (LangChain Expression Language)
chain = prompt | llm | parser

# 5. 결과를 도출한다 (위의 생성기들을 연결한 체인(prompt -> llm -> output)을 실행한다.)
inputs = {'company': 'high-tech startup', 'product': 'mobile games'}

result = chain.invoke(inputs)

print(f"최종결과:\n{result}")

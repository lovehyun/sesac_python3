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

# 4. 결과를 도출한다 (위의 생성기들을 연결 prompt -> llm -> output)
inputs = {'company': 'high-tech startup', 'product': 'mobile games'}

filled_prompt = prompt.format(**inputs) 
llm_output = llm.invoke(filled_prompt)
result_str = parser.invoke(llm_output)
result_csv = parser_csv.invoke(llm_output)

print(f'일반문자열\n{result_str}')
print(f'\n\nCSV 리스트\n{result_csv}')

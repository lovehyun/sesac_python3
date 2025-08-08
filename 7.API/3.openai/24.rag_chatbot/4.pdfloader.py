from dotenv import load_dotenv

# 채팅하기 위한 기본 라이브러리들
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 임베딩 추가 라이브러리
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma

# pip install pypdf

load_dotenv()

pdf_filename = "./DATA/Python_시큐어코딩_가이드(2023년_개정본).pdf"
loader = PyPDFLoader(pdf_filename)
pages = loader.load()

# print(pages)
# print(f"총 페이지 수: {len(pages)}")
# print(f"2페이지 내용 샘플:\n{pages[1].page_content}")
# print(f"2페이지 메타데이터:\n{pages[1].metadata}")

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    separator="\n\n", # 문서 분할 기준
    chunk_size=2000, # 최대 2000
    chunk_overlap=500, # 중복 500자 포함 (엄밀히는 토큰)
)
texts = text_splitter.split_documents(pages)
# print(texts[10])

embeddings = OpenAIEmbeddings()
store = Chroma.from_documents(texts, embeddings, collection_name="secure_coding_python", persist_directory="./chroma_db")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)

template = """
주어진 문서 내용을 바탕으로 질문에 답변해주세요

문서내용: {context}

질문: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
retriever = store.as_retriever(search_kwargs={'k':5}) # 유사 문서 5개를 바탕으로...
chain = ({"context": retriever, "question": RunnablePassthrough()}) | prompt | llm | StrOutputParser()

question = "시큐어코딩의 주요 기법들에 대해서 리스트 형태로 요약해서 설명해줘"

response = chain.invoke(question)
print("Q: ", question)
print("A: ", response)

# 이거.. 지금은 실행할때마다, 계속 DB를 생성하고, 누적해서 더하고 있음...
# => DB가 있으면 안만들고 로딩, 없으면 만들기
# => 답변줄때, 출처와 페이지를 함께 출력하기...
 
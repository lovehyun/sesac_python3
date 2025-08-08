from dotenv import load_dotenv

# 채팅하기 위한 기본 라이브러리들
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# 임베딩 추가 라이브러리
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# pip install langchain-community
# 백터DB 설치
# pip install chromadb

load_dotenv()

# 1. 문서 로딩
loader = TextLoader('./nvme.txt', encoding='utf-8')
documents = loader.load()
# print(documents)

# 2. 문서를 청크(chunk) 단위로 짜르기
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) # 1000/200, 2000/500
texts = text_splitter.split_documents(documents)
# print(texts)

# 3. 임베딩 하기
embeddings = OpenAIEmbeddings()
store = Chroma.from_documents(texts, embeddings, collection_name="nvme")
# print(store)

# 4. 실제로 질문할 준비..
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2) # RAG모델 에서는 온도를 낮추는게 일반적..

retriever = store.as_retriever()

template = """
다음 내용을 바탕으로 질문에 답변해주세요.
{context}

질문: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

# 5. 체인 구성: 사용자 질문은 question 에 담아서, 그대로 넘어감...
# context는 retriever로부터 추출해서 {context} 라는 공간에 채워줄예정..
# 프롬프트 -> LLM -> 응답
chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm

question = "NVME와 SATA의 차이점을 100글자로 요약해 주세요."
response = chain.invoke(question)
print(response.content)

# 6. 확인작업...
# context_docs = retriever.invoke(question)
# print('--- 검색된 문서는?? ---')
# for i, doc in enumerate(context_docs, start=1):
    # print(f"[=={i}==] {doc.page_content}\n")
    
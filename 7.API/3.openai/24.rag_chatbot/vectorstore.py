import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

load_dotenv()

# 필요한 글로벌 변수 선언
VECTOR_DB = './chroma_db'
COLLECTION_NAME = "my-data"
store = None

# 프롬프트 작성, LLM 호출하기 위한 체인

def initialize_vector_db():
    global store
    # 이전 DB가 있었으면? 로딩..
    if os.path.exists(VECTOR_DB) and os.listdir(VECTOR_DB):
        store = Chroma(collection_name=COLLECTION_NAME, embedding_function=OpenAIEmbeddings(), persist_directory=VECTOR_DB)
    else:
        # 없으면? 디렉토리 생성
        os.makedirs(VECTOR_DB, exist_ok=True)
    return True
    
def create_vector_db(file_path):
    global store
    # 벡터 DB 생성...
    # 1. 파일을 가져온다
    documents = PyPDFLoader(file_path).load()
    
    for doc in documents:
        doc.metadata['source'] = os.path.basename(file_path) # 경로 제외하고 파일명만 남기기
        
    # 2. 문서 분할한다
    texts = CharacterTextSplitter(chunk_size=100, chunk_overlap=20).split_documents(documents)
    print(texts)
    
    # 3. 임베딩 한다
    embeddings = OpenAIEmbeddings()
    if store:
        store.add_documents(texts)
    else:
        store = Chroma.from_documents(
            texts, embedding=embeddings, collection_name=COLLECTION_NAME, persist_directory=VECTOR_DB)
    
    print("벡터 DB가 정상적으로 생성되었습니다.")
    return store

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages([
    ("system", 
     "당신은 문서 기반 질의 응답 시스템 입니다."
     "아래 '문서' 를 참고하여 질문에 답변하세요."
     "\n\n문서:\n{context}\n\n"
     "만약 문서에 정보가 없다면, 지어내지 말고, '모르겠습니다' 라고 답하세요."),
    ("human", "{question}")
])
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

def answer_question(question):
    # LLM 에 질의 응답한다
    if store is None:
        return "문서가 로드되지 않았습니다. 먼저 PDF를 업로드 해주세요."
    
    docs = store.similarity_search(question, k=5)
    context = "\n\n\n".join([doc.page_content for doc in docs])
    for i, d in enumerate(docs, 1):
        print(f"문서 #{i} - {d}")
        
    
    # 체인 호출, 질문과 함께...
    result = chain.invoke({"context": context, "question": question})
    
    return result

def delete_file_from_vstore(filename):
    # NoSQL 기반의 DB에서 자료 삭제하는것과 동일함 (예, mongodb)
    store._collection.delete(where={"source": filename})
    
    # 백터DB가 persist 옵션이 켜져 있으면? 저장..
    if hasattr(store, "persist"):
        store.persist()

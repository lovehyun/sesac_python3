from dotenv import load_dotenv
import os

from flask import Flask, request, jsonify

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

# app = Flask(__name__, static_folder='static', static_url_path='static')
app = Flask(__name__, static_folder='public', static_url_path='')
llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0.7
)

# 프롬프트 템플릿 만들기
summary_prompt = PromptTemplate.from_template(
    """다음 목록을 기반으로 간결한 요약을 작성하시오.

리뷰목록:
{reviews_text}
"""
)

translate_prompt = PromptTemplate.from_template(
    """다음 한국어 문장을 기반으로 {target_lang_name} 으로 번역하시오.
    
{summary_ko}
"""
)

# 체인 구성
summary_chain = summary_prompt | llm
translate_chain = translate_prompt | llm

# 최종 원하는 체인
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

summary_then_translate_chain = (
    {"summary_ko": summary_prompt | llm | RunnableLambda(lambda m: m.content),
     "target_lang_name": RunnablePassthrough() }
    #  "target_lang_name": RunnableLambda(lambda x: x["target_lang_name"]) }
    | translate_prompt
    | llm
    | RunnableLambda(lambda m: m.content)
)

reviews = [] # 사용자 후기를 저장할 DB

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    rating = data.get('rating')
    opinion = data.get('opinion')
    
    reviews.append({'rating': rating, 'opinion': opinion})
    
    return jsonify({'message':'성공적으로 저장됨'})

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    return jsonify({'reviews': reviews})

@app.route('/api/ai-summary', methods=['GET'])
def get_ai_summary():
    target_lang = request.args.get('lang', 'ko')
    lang_name_map = {
        'ko': '한국어',
        'en': '영어',
        'ja': '일본어',
        'zh': '중국어',
        'fr': '프랑스어',
        'it': '이탈리아어',
    }
    
    lang_name = lang_name_map.get(target_lang, '한국어')
    print(f'언어: {target_lang}, 언어명: {lang_name}')
    
    # 미션1. 프런트에서 보낸 언어 "코드값" 으로, 원하는 언어로 매핑을 한다.
    # 미션2. 그걸 기반으로, GPT에게 해당 언어로 요약을 만들어 달라고 한다.
    #       하나의 프롬프로 할지, 아니면 두번의 스탭으로 나눠서 (한번은 요약, 한번은 번역) 이렇게 할지 고민해보기...
    
    if not reviews:
        return jsonify({'summary': '리뷰가 없습니다.', 'averageRating': 0.0})

    average_rating = sum(r['rating'] for r in reviews) / len(reviews)
    reviews_text = '\n'.join([f"별점: {r['rating']}, 내용: {r['opinion']}" for r in reviews])
    
    print("리뷰내용 통합: ", reviews_text)
    
    # 아래도 try catch 로 꼭 감싸야 함.. key가 없거나, 돈이 다 떨어졌거나, 서버가 죽었거나, 여러가지 이유로 요청에 실패할수 있음.
    # 두번 나누어서 호출하기
    # response_summary = summary_chain.invoke({'reviews_text': reviews_text}).content
    # print("요약내용: ", response_summary)
    
    # response_translated = translate_chain.invoke({'summary_ko': response_summary, 'target_lang_name': lang_name}).content
    # print("요약번역내용: ", response_translated)
    
    # 한번에 두가지를 체이닝해서 호출하기
    response_translated = summary_then_translate_chain.invoke({
        "reviews_text": reviews_text,
        "target_lang_name": lang_name
    })
    
    return jsonify({'summary': response_translated, 'averageRating': average_rating})

if __name__ == '__main__':
    app.run(port=5000, debug=True)

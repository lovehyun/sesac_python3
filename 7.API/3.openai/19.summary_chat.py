from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda

load_dotenv()

# 1. 템플릿 정의
template = "다음 문장을 3줄로 요약하시오.\n\n{article}"
# prompt = ChatPromptTemplate.from_messages([
#     HumanMessagePromptTemplate.from_template(template)
# ])

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("당신은 긴 장문에 대해서 요약하는 전문가 입니다."),
    HumanMessagePromptTemplate.from_template(template)
])


# 2. 모델 정의
llm = ChatOpenAI(temperature=0.5) # 요약할꺼니깐, 창의력 줄이고, 펙트 위주로...

# 3. 체인 생성
print_line_by_line = RunnableLambda(
    lambda x: {
        "summary": [line.strip() for line in x.split('\n') if line.strip()]
    }
)

chain = prompt | llm | RunnableLambda(lambda x: {"summary": x.content.strip()})
# chain = prompt | llm | print_line_by_line

# 4. 입력 및 호출
input_text = {
    "article": """
애플이 올해 가을 출시 예정인 아이폰17 프로 라인업에 고성능 이미지 센서, 향상된 배터리 설계, AI 최적화를 위한 사양 업그레이드를 대거 적용한다.

4일(현지시간) 복수의 미국IT전문매체들에 따르면 애플은 아이폰17 프로 및 프로 맥스에 자사 설계의 커스텀 이미지 센서를 도입하고, 48MP 망원 카메라 및 24MP 전면 카메라 등 카메라 전면 개편을 시도한다고 전했다. AI 처리 성능을 강화하기 위해 최대 12GB RAM을 탑재하고, 발열 제어를 위한 베이퍼 챔버와 그래파이트 냉각시트를 적용하는 등 AI 하드웨어 플랫폼으로서의 완성도를 높이고 있다는 설명이다.

그 중에서도 특히 눈에 띄는 변화는 이미지 센서다. 애플은 최근 ‘고동적 범위(HDR) 및 저노이즈를 갖는 스택형 픽셀 이미지 센서’라는 제목의 특허를 출원했다. 이 센서는 센서 다이와 로직 다이로 분리된 스택 구조와 픽셀 단위의 열 잡음 제거 회로, 그리고 고휘도·저휘도 영역을 동시에 처리할 수 있는 LOFIC(측면 오버플로 통합 커패시터) 기술이 핵심이다. 이를 통해 최대 20스톱의 다이내믹레인지를 구현할 수 있어, 기존 아이폰은 물론 헐리우드급 시네마 카메라 수준을 능가할 수 있다는 평가도 나온다. 현재 아이폰 카메라는 약 12스톱, 전문 시네마 카메라는 14~17스톱 수준이다.

이러한 고성능 이미지 센서는 기존 소니 센서를 대체해 애플이 설계부터 생산·튜닝까지 모든 이미지 파이프라인을 통제할 수 있게 될 가능성을 내포한다. 이는 기존에 인텔·퀄컴 칩을 탈피해 자사 설계를 택한 M1·A 시리즈와 유사한 전략으로, 애플의 수직통합 기조를 카메라까지 확장하는 움직임으로 해석된다.
    """
}

result = chain.invoke(input_text)
print("최종결과: ", result)

# lines = result['summary'].split('\n')
# for line in lines:
#     print(line)

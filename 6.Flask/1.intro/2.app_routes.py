from flask import Flask

app = Flask(__name__)

@app.route('/')   # 사용자가 / 에 접속하면, 이 아래 함수를 호출해줘
def home():
    return "<h1>Hello, Flask!</h1>"

@app.route('/user')   # 사용자가 /user 에 접속하면, 이 아래 함수를 호출해줘
def user():
    return "<h1>Hello, User!</h1>"

@app.route('/user/<username>')
def greet_user(username):  # 위에 flask 데코레이터에서 정한 변수명 <변수명> 으로 함수 인자로 전달해줌
    return f"<h1>Hello, {username}님!</h1>" # 서버 사이드 랜더링.. (서버에서 필요한 HTML을 그때그때 만들어 준것)

@app.route('/user/<int:age>') # 내가 따로 정의하지 않으면 문자열임. 그래서 바꾸고 싶으면 타입 지정 가능
def greet_with_age(age):  # 위에 flask 데코레이터에서 정한 변수명 <변수명> 으로 함수 인자로 전달해줌
    return f"<h1>Hello, {age}살 아무개님!</h1>" # 서버 사이드 랜더링.. (서버에서 필요한 HTML을 그때그때 만들어 준것)

@app.route('/user/<float:weight>') # 내가 따로 정의하지 않으면 문자열임. 그래서 바꾸고 싶으면 타입 지정 가능
def greet_with_weight(weight):  # 위에 flask 데코레이터에서 정한 변수명 <변수명> 으로 함수 인자로 전달해줌
    # 이렇게 함수 내부에 비즈니스 로직을 구현하는것...
    
    if weight > 60:
        message = "뚱뚱한"
    elif weight < 40:
         message = "날씬한"
    else:
        message = ""
        
    # 결론은, 원하는 메세지 (결론=결과물) 을 만들어 냄..
    return f"<h1>Hello, {weight}kg {message} 아무개님!</h1>" # 서버 사이드 랜더링.. (서버에서 필요한 HTML을 그때그때 만들어 준것)

@app.route('/user/<name>/<int:Age>/<float:weight>')
def greet_user_with_detail(name, age, weight):
    return f"<H1>안녕하세요</H1><H2>사용자정보</H2><UL><LI>이름: {name}</LI><LI>나이: {age}</LI><LI>몸무게: {weight}</LI></UL>"

@app.route('/product')   # 사용자가 /product 에 접속하면, 이 아래 함수를 호출해줘
def product():
    return "<h1>Hello, Product!</h1>"

if __name__ == '__main__':
    print("여기가 메인 함수")
    app.run(debug=True) # 절대로 이대로 커밋하면 안됨!! 꼭 끝다음에 커밋해야함.

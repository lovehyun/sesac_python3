# pip install flask

from flask import Flask

app = Flask(__name__)

@app.route('/')   # 사용자가 / 에 접속하면, 이 아래 함수를 호출해줘
def home():
    return "<h1>Hello, Flask!</h1>"

if __name__ == '__main__':
    print("여기가 메인 함수")
    app.run()

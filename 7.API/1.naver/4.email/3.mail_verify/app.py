# pip install flask-mail
from flask import Flask, request, jsonify, render_template, session
from flask_mail import Mail, Message

from dotenv import load_dotenv
import os
import random

load_dotenv()

app = Flask(__name__)
app.secret_key = 'abcd1234'

app.config['MAIL_SERVER'] = os.getenv("NAVER_MAIL_SERVER")
app.config['MAIL_PORT'] = os.getenv("NAVER_MAIL_PORT")
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("NAVER_EMAIL")
app.config['MAIL_PASSWORD'] = os.getenv("NAVER_PASSWORD")
mail = Mail(app)
print(app.config['MAIL_SERVER'])
print(app.config['MAIL_PORT'])

@app.route('/')
def signup():
    return render_template('index.html')

@app.route('/send-code', methods=['POST'])
def send_code():
    email = request.json.get('email') # 사용자로부터 받아오기
    print('입력한 이메일: ', email)
    
    # 미션1. 6자리 숫자 랜덤값 만들기
    code = str(random.randint(100000, 999999))
    
    # 미션1-1. 세션에 우리의 랜덤 코드...
    session['auth_code'] = code
    print('발송한 코드는: ', code)

    msg = Message("회원가입 인증 코드", sender=app.config['MAIL_USERNAME'], recipients=[email])
    msg.body = f"인증 코드: {code}"
    mail.send(msg)

    return jsonify({"message": "인증 코드가 전송되었습니다."})

@app.route('/verify-code', methods=['POST'])
def verify_code():
    # 미션2. 내가 보낸 코드와 같은지 확인하고
    code = request.json.get('code') # 사용자로부터 받아오기
    
    # 미션2-1. 저장된 세션으로부터 코드 가져와서.. 사용자 입력, 내가 저장해둔거랑 같은지 확인..
    stored_code = session.get('auth_code', None)
    
    print(f"저장된 코드값: {stored_code}, 사용자 입력: {code}")
    if (stored_code == code):
        return jsonify({"message": "인증성공"})

    return jsonify({"message": "인증실패"})

if __name__ == "__main__":
    app.run(debug=True)

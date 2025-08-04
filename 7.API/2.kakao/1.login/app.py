from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for, session
import requests
import os
import json

load_dotenv()

app = Flask(__name__)
app.secret_key = '아무거나'

KAKAO_CLIENT_ID = os.getenv("KAKAO_REST_API_KEY")
KAKAO_CLIENT_SECRET = os.getenv("KAKAO_CLIENT_SECRET")
KAKAO_REDIRECT_URI = os.getenv("KAKAO_REDIRECT_URI")

@app.route('/')
def index():
    kakao_auth_url = (
        # 카카오 로그인 주소 엔드포인트 찾아오기, 또한 필요한 입력값들 확인하기
        f"https://kauth.kakao.com/oauth/authorize?"
        f"response_type=code&client_id={KAKAO_CLIENT_ID}"
        f"&redirect_uri={KAKAO_REDIRECT_URI}&scope=profile_nickname,profile_image"
    )
    
    return render_template("index.html", kakao_auth_url=kakao_auth_url)

@app.route('/auth/kakao/callback')
def callback():
    code = request.args.get("code")
    print("코드값: ", code)
    if not code:
        return "인가 코드가 없습니다.", 400
    
    # 카카오에게 코드 검증후 토큰을 발급받을 엔드포인트 및 입력값 확인하기
    token_url = "https://kauth.kakao.com/oauth/token"
        
    data = {
        "grant_type": "authorization_code",
        "client_id": KAKAO_CLIENT_ID,
        "redirect_uri": KAKAO_REDIRECT_URI,
        "code": code
    }
    # 만약 보안 인증을 위해서 CLIENT_SECRET 사용을 켰다면?? 이거도 추가

    headers = {"Content-Type": "application/x-www-form-urlencoded;charset=utf-8"}
    
    token_res = requests.post(token_url, data=data, headers=headers).json()
    print("인증토큰:", token_res)
    
    access_token = token_res.get('access_token')
    
    # 성공했으면? 사용자 정보 요청하기
    # 사용자 정보 가져오기 위한 엔드포인트
    user_info_url = "https://kapi.kakao.com/v2/user/me"
    headers = {"Authorization": f"Bearer {access_token}"}
    user_info = requests.get(user_info_url, headers=headers).json() # 위의 변수와 인자값들 채워넣기
    
    # 로그인 성공!!
    print("사용자정보:", user_info)
    
    session['user'] = user_info
    # return "로그인 성공" # 어디로 보낼지 알아서 처리
    return redirect(url_for("profile"))

@app.route("/profile")
def profile():
    user = session.get('user')
    if not user:
        return redirect(url_for('index'))
    
    # 위에 내용 다 끝나면?? 사용자 정보 저장하고, 수정하고 등등 기능 추가
    return render_template("profile.html", user=user)

# 로그아웃 추가하기

if __name__ == "__main__":
    app.run(debug=True)
    
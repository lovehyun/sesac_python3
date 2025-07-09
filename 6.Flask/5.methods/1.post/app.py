from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 미션1. 사용자 목록 완성
# 미션2. 로그인할때 사용자 ID/PW 맞는지 체크
# 미션3. 맞으면 로그인성공인거니 성공페이지로 이동 (안녕하세요 OOO님 <== 이름)
#       실패시, 로그인 실패라고 출력

# 사용자 목록
users = [
    # 여기 사용 이름, 아이디, 암호 를 3명이상의 사용자를 여기 넣고
    # dict 로 key, value 형태로...
    {'name': '엘리스', 'id': 'alice', 'pw': 'alice'},
    {'name': '밥', 'id': 'bob111', 'pw': 'bob1234'},
    {'name': '챨리', 'id': 'charlie', 'pw': 'hello'}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # POST 에 대한 처리
        id = request.form["id"]
        pw = request.form["password"]
        print("입력된 ID/PW: ", id, pw)
        
        # 일반적인 for / if 구문
        # user = None
        # for u in users:
        #     if u['id'] == id and u['pw'] == pw:
        #         user = u
        #         break
            
        # 좀 더 pythonic 하게 짜면...
        user = next((u for u in users if u['id'] == id and u['pw'] == pw), None)
        print('검색된 사용자: ', user)
        
        if user:
            error = None
        else:
            error = "ID/PW 가 올바르지 않습니다."
            
        return render_template('user.html', user=user, error=error)
        # return redirect(url_for("user", user=user))
        # return render_template('user.html', user=user)
    else:
        # POST가 아닐때에 대한 처리 => GET일때의 처리
        return render_template('login.html')

@app.route('/user')
@app.route('/user/<user>')
def user(user=None): # 초기값 할당
    if user:
        error = None
    else:
        error = "ID/PW 가 올바르지 않습니다."
    print('프런트전달전: ', user)
    return render_template('user.html', user=user, error=error)

@app.route('/product')
def product():
    return render_template('product.html')  

if __name__ == "__main__":
    app.run(debug=True)

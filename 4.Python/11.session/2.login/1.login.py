from flask import Flask, render_template, request, redirect, url_for
from flask import session

app = Flask(__name__)
app.secret_key = 'this-is-my-important-password'

users = [
    {'name': 'Alice', 'id': 'alice', 'pw': 'alice'},
    {'name': 'BoB', 'id': 'bob', 'pw': 'bob1234'},
    {'name': 'Charlie', 'id': 'charlie', 'pw': 'hello'},
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if session.get('user'):
        return redirect(url_for('welcome'))
    
    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')
        # print(id, password)
        
        # 사용자 목록과 매칭
        user = next((u for u in users if u['id'] == id and u['pw'] == password), None)
        if user:
            session['user'] = user  # 로그인한 사용자 정보를 세션에 저장
            return redirect(url_for('welcome'))
        else:
            return '로그인에 실패하였습니다.'
        
    return render_template('index.html')

@app.route('/dashboard')
def welcome():
    user = session.get('user')
    if user:
        return render_template('dashboard.html', name=user['name'])
    else:
        return redirect(url_for('index'))

@app.route('/profile')
def profile():
    user = session.get('user')   # 이건 아까 우리가 저장한 정보
    if user:
        return f'당신은 아까 왔던 사용자군요. {user}'
    else:
        return f"로그인이 안된 사용자입니다."

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))
    
# 미션1. 로그인 된 사용자는 dashboard.html 을 만들어서.
#        "안녕하세요, OOO님" <-- 세션에 있는 정보를 기반으로...
# 미션2. / 에 접속해서 로그인된 사용자면 바로 dashboard로 보내기...
# 미션3. 로그아웃 구현하기.
#        "안녕하세요, OOO님"  밑에줄에... "로그아웃" 추가 a href 로 /logout 으로

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from flask import session

app = Flask(__name__)
app.secret_key = 'sesac'

users = [
    {'name': 'MyName', 'id': 'user', 'pw': 'password'}
]

@app.route('/')
def home():
    user = session.get('user')
    return render_template('index.html', user=user)

@app.route('/user')
def user():
    user = session.get('user')
    if user:
        return render_template('user.html', user=user)
    else:
        return redirect(url_for('login'))  # 어디로 보낼지, 뭐라고 출력할지, 내맘임..

@app.route('/login', methods=["GET"])
def login():
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def login_submit():
    input_id = request.form.get('id')
    input_pw = request.form.get('password')
    
    user = next((u for u in users if u['id'] == input_id and u['pw'] == input_pw), None)
    if user: # 성공
        session['user'] = user  # 사용자 정보를 모두다 저장함.
        return redirect(url_for("user"))
    else: # 실패
        return render_template('login.html', error="ID 또는 비밀번호가 올바르지 않습니다.")

@app.route('/logout')
def logout():
    session.pop('user', None)  # user가 없으면 KeyError 가 날 수 있음.. 그래서 없을때 None 반환..
    return redirect(url_for('home'))

@app.route('/product')
def product():
    user = session.get('user')
    return render_template('product.html', user=user)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, flash 
from flask import session
from datetime import timedelta
import sqlite3
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcd1234'
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

DB_FILENAME = 'users.db'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def get_user(username, password):
    conn = sqlite3.connect(DB_FILENAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    hashed_pw = hash_password(password)
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_pw)) # 비밀번호를 해시로 바꿔서 물어보기...
    user = cur.fetchone()
    conn.close()
    return user

def get_user_by_username(username):
    conn = sqlite3.connect(DB_FILENAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=?", (username, ))
    user = cur.fetchone()
    conn.close()
    return user

def create_user(username, password, name):
    hashed_pw = hash_password(password)
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password, name) VALUES (?,?,?)",
                (username, hashed_pw, name))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('id')
        user_pw = request.form.get('pw')
        
        user = get_user(user_id, user_pw)
        if user:
            session['user'] = {'id': user['id'], 'name': user['name']}
            flash('로그인에 성공했습니다.', 'success')
            return redirect(url_for('user'))
        
        flash('ID/PW가 일치하지 않습니다', 'danger')
        return redirect(url_for('index'))

@app.route('/user')
def user():
    if 'user' in session:
        # user = session['user']
        user = session.get('user')
        # user = session.get('user', None)
        
        return render_template('user.html', name=user['name'])
    
    flash('비정상 접근입니다. 로그인을 필요로 합니다.', 'danger')
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
        flash('정상적으로 로그아웃 되었습니다.', 'success')
    else:
        flash('이미 로그아웃 되었습니다.', 'warning')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form.get('id')
        user_pw = request.form.get('pw')
        user_pw2 = request.form.get('pw2')
        name = request.form.get('name')
        
        if not user_id or not user_pw or not user_pw2 or not name:
            flash('모든 필드를 입력해주세요', 'warning')
            return redirect(url_for('register'))
        
        if user_pw != user_pw2:
            flash('비밀번호가 일치하지 않습니다', 'danger')
            return redirect(url_for('register'))
        
        if get_user_by_username(user_id):
            flash('이미 존재하는 사용자 아이디 입니다.', 'danger')
            return redirect(url_for('register'))
        
        create_user(user_id, user_pw, name)
        flash('회원가입이 완료되었습니다. 로그인 해 주세요.', 'success')
        return redirect(url_for('index'))
        
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

# curl 127.0.0.1:5000/set-session/user1 --cookie-jar cookie.txt
# curl 127.0.0.1:5000/set-session/user1 -c cookie.txt
# curl 127.0.0.1:5000/get-session --cookie cookie.txt
# curl 127.0.0.1:5000/get-session -b cookie.txt

from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'my-secret-key' # 세션 암호화를 위한 키 (내가 관리하고, 내가 암호화 하고 내가 복호화 하고, 즉 외부에 노출되면 안됨)

@app.route('/set-session/<username>')
def set_session(username):
    session['username'] = username
    return '세션이 저장되었습니다.'

@app.route('/get-session')
def get_session():
    if 'username' in session:
        return f"세션정보: {session['username']}"
    else:
        return f"저장된 정보가 없습니다."

@app.route('/clear-session')
def del_session():
    session.pop('username', None) # 세션에서 값 삭제
    return f"세션 정보가 삭제되었습니다."

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

# 더미 유저 100명 생성
users = [
    { 'id': i, 'name': f'User{i}', 'age': 20+i % 10, 'phone': f'010-0000-{str(i).zfill(4)}'} for i in range (1, 105)
]

@app.route('/')
def index():
    return render_template('users.html', users=users, page=None)

# http://localhost:5000/pages/1
@app.route('/pages/<int:page>')
def pages(page):
    # 1.입력받는다
    # 2.프로세싱한다
    # 3.출력한다
    
    per_page = 10
    start = (page - 1) * per_page
    end = start + per_page
    
    users_on_page = users[start:end]
    
    return render_template('users.html', users=users_on_page, page=page)

if __name__ == "__main__":
    app.run(debug=True)

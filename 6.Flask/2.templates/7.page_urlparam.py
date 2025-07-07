from flask import Flask, render_template

app = Flask(__name__)

# 더미 유저 100명 생성
users = [
    { 'id': i, 'name': f'User{i}', 'age': 20+i % 10, 'phone': f'010-0000-{str(i).zfill(4)}'} for i in range (1, 101)
]

# http://localhost:5000/pages/1
@app.route('/')
def index():
    page = None
    return render_template('users.html', users=users, page=page)

if __name__ == "__main__":
    app.run(debug=True)

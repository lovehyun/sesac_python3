# pip install flask-sqlalchemy

from flask import Flask, render_template, request, redirect
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db.init_app(app)

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')
    age = int(request.form.get('age'))

    # 필요한 에러체크를 더 넣는게 좋음 - 중복사용자/누락된 데이터 등등 (지금은 생략)
    new_user = User(name=name, age=age)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/')  # redirect(url_for('index')) 가 좀 더 나은 코드이기는 함.

@app.route('/edit_user/<int:id>')
def edit_user(id):
    user = db.session.get(User, id)
    # 사용자가 없으면 처리할것.. (지금은 넘어감)
    return render_template('edit_user.html', user=user)

@app.route('/update_user/<int:id>', methods=['POST'])
def update_user(id):
    user = db.session.get(User, id)
    # 사용자가 없으면 처리할것.. (지금은 넘어감)

    name = request.form.get('name')
    age = request.form.get('age')
    user.name = name
    user.age = int(age)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_user(id):
    user = db.session.get(User, id)
    if user:
        db.session.delete(user)
        db.session.commit()
    else:
        print('사용자 없음: ', id)

    return redirect('/')

if __name__ == '__main__':
    # app = create_app()
    app.run(debug=True)

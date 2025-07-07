from flask import Flask, jsonify
# from flask import jsonify

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'mobile': '050-1234-5678'},
    {'name': 'Bob', 'age': 30, 'mobile': '050-2222-5678'},
    {'name': 'Charlie', 'age': 35, 'mobile': '050-3333-5678'},
]

@app.route('/')
def index():
    return jsonify(users)

@app.route('/user/<name>')
def get_user_by_name(name):
    print("이름", name)
    
    user = None
    for u in users:
        if name.lower() == u['name'].lower():  # 입력에 소문자, DB에 소문자로 변환해서 비교
            user = u
            break  # 반복문을 중단
        
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/user/<int:age>')
def get_user_by_age(age):
    print("나이", age)
    
    user = None
    for u in users:
        if age == u['age']:
            user = u
            break  # 반복문을 중단
        
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)

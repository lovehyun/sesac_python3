from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'mobile': '050-1234-1234'},
    {'name': 'Alice', 'age': 35, 'mobile': '050-5555-1234'},
    {'name': 'Bob', 'age': 30, 'mobile': '050-2222-5678'},
    {'name': 'Charlie', 'age': 35, 'mobile': '050-3333-5678'},
    {'name': 'David', 'age': 30, 'mobile': '050-4444-5678'},
]

# 미션1. 사용자 목록을 테이블로 그린다
# <table border="1"> <tr> <td>
# 미션2. 입력폼을 하나 만들고, 사용자 이름으로 원하는 사용자만 골라낸다


# http://localhost:5000/?name=aaa&age=22

@app.route('/')  # GET 파라미터 요청이 함께 온다는 것...
def home():
    name = request.args.get('name')
    age = request.args.get('age')
    phone = request.args.get('phone')
    
    print(f"이름: {name}, 나이: {age}, 전화번호 {phone}")
    filtered_users = users
    
    # 전체목록 (100) -> 이름과 나이
    # 1. 전체목록 (100) -> 이름비교
    # 2. 이름매칭(30) -> 나이비교
    # 3. 나이매칭(5)
    if name:
        # 이름으로 비교하기
        filtered_users = [u for u in filtered_users if name.lower() == u['name'].lower()]
        
    if age:
        # 나이로 비교하기
        filtered_users = [u for u in filtered_users if int(age) == u['age']]
    
    if phone:
        # 전화번호로 비교하기 (in 을 사용해서 일부 매칭도 가능)
        filtered_users = [u for u in filtered_users if phone in u['mobile']]
    
    return render_template('index9.html', users=filtered_users)

if __name__ == '__main__':
    app.run(debug=True)

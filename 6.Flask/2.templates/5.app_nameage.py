from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'mobile': '050-1234-5678'},
    {'name': 'Alice', 'age': 35, 'mobile': '050-5555-5678'},
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
    
    print(f"이름: {name}, 나이: {age}")
    filtered_users = users
    
    # 아래는 한줄짜리 pythonic 한 스타일 코드...
    # 0 0 0
    # 0 0 1
    # 0 1 0
    # 0 1 1
    # 1 0 0
    # 1 0 1
    # 1 1 0
    # 1 1 1
    
    # 이런 로직을 어떻게 이렇게 하나하나 비교 안하고 할수 없을까???
    # 설계적으로, 논리적으로는 좋지 않음.. 왜?? 항목의 제곱수로 늘어나는 조합에 대한 비교가 필요함..
    # 제곱수가 아니고, 그냥 그 항목의 갯수만큼
    
    if name and age and phone:
        filtered_users = [u for u in users if u['name'].lower() == name.lower() and u['age'] == int(age)]
    elif name and age:
        filtered_users = [u for u in users if u['name'].lower() == name.lower() and u['age'] == int(age)]
    elif name and phone:
        filtered_users = [u for u in users if u['name'].lower() == name.lower() and u['age'] == int(age)]
    elif age and phone:  # 여기서 부터 아래까지가 일단...
        filtered_users = [u for u in users if u['name'].lower() == name.lower() and u['age'] == int(age)]
    elif name:
        filtered_users = [u for u in users if u['name'].lower() == name.lower()]
    elif age:
        filtered_users = [u for u in users if u['age'] == int(age)]
    
    return render_template('index5.html', users=filtered_users)

if __name__ == '__main__':
    app.run(debug=True)

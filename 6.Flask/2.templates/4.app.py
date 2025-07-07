from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'mobile': '050-1234-5678'},
    {'name': 'Bob', 'age': 30, 'mobile': '050-2222-5678'},
    {'name': 'Charlie', 'age': 35, 'mobile': '050-3333-5678'},
]

# 미션1. 사용자 목록을 테이블로 그린다
# <table border="1"> <tr> <td>
# 미션2. 입력폼을 하나 만들고, 사용자 이름으로 원하는 사용자만 골라낸다

# http://localhost:5000/?name=ccc  <-- URL은 / 에서 끝.. 나머지는 ? GET파라미터
# http://localhost:5000/name/ccc   <-- URL 리소스를 통해서 입력 = 라우트 경로로 파싱

@app.route('/')  # GET 파라미터 요청이 함께 온다는 것...
def home():
    name = request.args.get('name')
    print("이름: ", name)
    filtered_users = users
    # for u in users:
    #     if u['name'].lower() == name.lower():
    #         filtered_users = [u]
    #         break
    
    # 아래는 한줄짜리 pythonic 한 스타일 코드...
    if name:
        filtered_users = [u       for u in users      if u['name'].lower() == name.lower()]
        
    return render_template('index4.html', users=filtered_users)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# db를 안쓸때는...
users = []   # 예, [{'id': 1, 'name': '홍길동', 'age': 30 }]
next_id = 1  # id 자동 증가

@app.route('/', methods=['GET', 'POST'])
def index():
    global next_id  # 글로벌 변수에 write 를 할때는 이 선언이 필요함. read 할때는 필요 없음.
                    # 변수 안에 멤버가 수정될때는 무관함. 해당 변수 자체가 변경될때는 global 선언이 필요함.

    if request.method == 'POST':
        # POST 요청 처리하기
        name = request.form['name']
        age = int(request.form['age'])
        
        # 사용자 추가
        users.append({'id': next_id, 'name': name, 'age': age})
        next_id += 1 # 자동 증가 (다음을 위해서...)
        
        return redirect('/') # 추가 끝났으면 그 페이지 다시 불러오기
    
    # GET 요청 처리하기
    print('원래코드전체사용자:', users)
    return render_template('index.html', users=users)

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    # global users
    # 미션1. users 라는 저 변수를 뒤져서. user_id 를 찾아서, 지운다
    for i, user in enumerate(users):
        if user['id'] == user_id:
            print('삭제할사용자찾음:', user, i)
            del users[i]
            break
    print('전체목록조회: ', users)
    
    # 수업용으로 좋고, 실용적이지 않음. 왜? 하나 지울려고 모든 리스트를 새로 만들어야 함. 속도가 느림
    # users = [u for u in users if u['id'] != user_id]
    return redirect('/')

@app.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    global users
    
    user = next((u for u in users if u['id'] == user_id), None)
    print(user)
    
    if request.method == 'POST':
        # 미션3. POST = 실제 수정하는 코드
        if not user:
            return "사용자를 찾을 수 없습니다.", 404
        
        user['name'] = request.form['name']
        user['age'] = int(request.form['age'])
        
        return redirect('/')
        
    # 미션2. GET = 수정을 위한 사용자 정보를 보여주는 곳
    # 공통이라서 위로 올렸음... 이 코드 맨 위에로... next()
    
    # users라는 저 변수를 뒤져서, user_id를 찾아서, 수정한다...
    return render_template('update_user.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)

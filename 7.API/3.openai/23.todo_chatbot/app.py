from flask import Flask, request, jsonify

app = Flask(__name__, static_folder='public', static_url_path='')

# 내 메모 리스트 담을곳
todos = []
next_id = 1

@app.route('/')
def home():
    return app.send_static_file('index.html')

# READ = todo 리스트 가져오기
@app.route('/api/todo', methods=['GET'])
def get_todos():
    return jsonify(todos)

# CREATE = todo 리스트 생성하기
@app.route('/api/todo', methods=['POST'])
def add_todo():
    global next_id
    
    # 1. 입력값 가져온다
    data = request.get_json()
    task = data.get('text')
    print('할일: ', task)
    # 2. 입력값 프로세싱 및 저장
    new_todo = {'id': next_id, 'task': task, 'done': False}
    todos.append(new_todo)
    next_id += 1
    # 3. 결과 반납
    return jsonify({'success': '성공적으로 추가됨'})

# UPDATE = todo 리스트 done/undone (toggle) 처리
@app.route('/api/todo/<int:todo_id>', methods=['PUT'])
def toggle_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['done'] = not todo['done']
            return jsonify({'success': f"ID: {todo_id} 를 {todo['done']} 처리 완료"})
            
    return jsonify({'error': '아직 구현안됨'})

# DELETE = todo 아이템 삭제하기
@app.route('/api/todo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todos.remove(todo)
            return jsonify({'success': '성공적으로 삭제 완료'})
        
    return jsonify({'error': f'해당 항목이 없음 (ID: {todo_id}) '}), 404

# 미션1. 투두의 CRUD 완성
# 미션2. 챗봇을 프런트에 추가하고 /api/chat 을 추가할 차례가 되었는데...
#        근데, 완전히 다른 요청을 여기 한 파일에서 할거냐??
# 미션2-1. 어떻게 라우트를 분리할까? todo 서비스와 chat 서비스를 분리하자
#         routes 를 분리하려면?? blueprint를 도입한다
# 미션3. 채팅 아무 말이나 받아서 GPT에게 주고, 요청 받아서 화면에 뿌리기

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify

from routes.chatbot_routes import chatbot_bp
from routes.todo_routes import todo_bp

app = Flask(__name__, static_folder='public', static_url_path='')

app.register_blueprint(todo_bp)
app.register_blueprint(chatbot_bp)

@app.route('/')
def home():
    return app.send_static_file('index.html')

# 미션1. 투두의 CRUD 완성
# 미션2. 챗봇을 프런트에 추가하고 /api/chat 을 추가할 차례가 되었는데...
#        근데, 완전히 다른 요청을 여기 한 파일에서 할거냐??
# 미션2-1. 어떻게 라우트를 분리할까? todo 서비스와 chat 서비스를 분리하자
#         routes 를 분리하려면?? blueprint를 도입한다
# 미션3. 채팅 아무 말이나 받아서 GPT에게 주고, 요청 받아서 화면에 뿌리기

if __name__ == '__main__':
    app.run(debug=True)

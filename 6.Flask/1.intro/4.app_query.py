from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/search')  # /search?q=apple&page=2
def search():
    # 사용자가 입력한 다양한 쿼리 파라미터를 처리하는것
    query = request.args.get('q')
    # page = request.args.get('page')
    page = request.args.get('page', default=1, type=int) # query구문에 해당 키가 없어도, 기본값 설정하기
    
    print(query, page)
    
    return 'Hello'

if __name__ == '__main__':
    app.run(debug=True)

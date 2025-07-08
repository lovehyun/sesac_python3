from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # name = request.args.get('name') # GET 파라미터(아규먼트=argements) 를 받는 방식임
    name = request.form.get('name') # POST 로 form(폼) 이 전달된거 안에서 name이 키인것을 주시오~
    age = request.form.get('age') # POST 로 form(폼) 이 전달된거 안에서 키가 age인 것을 주시오~
    
    print(request)
    
    return f'안녕하세요 {age} 세 {name} 님'

if __name__ == '__main__':
    app.run(debug=True)

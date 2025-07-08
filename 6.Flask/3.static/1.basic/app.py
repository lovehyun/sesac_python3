from flask import Flask, render_template

app = Flask(__name__)

# 1. static 폴더는 바꿀수는 있지만 굳이 바꿀 필요는 없음
# 2. static 이라고 폴더명을 정해주며, 그곳은 자동으로 외부에 노출된다 (img, html, css, js)
# 3. 그래서 index안에서 static을 전달할때는 하드코딩해도 동작은 하지만,
#    그것보다 url_for('static',...) 이라고 해서 전달하는게 더 좋은 코딩이다.

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

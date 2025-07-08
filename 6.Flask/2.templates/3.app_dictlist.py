from flask import Flask, render_template

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'mobile': '050-1234-5678'},
    {'name': 'Bob', 'age': 30, 'mobile': '050-2222-5678'},
    {'name': 'Charlie', 'age': 35, 'mobile': '050-3333-5678'},
]


@app.route('/')
def home():
    return render_template('index3.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)

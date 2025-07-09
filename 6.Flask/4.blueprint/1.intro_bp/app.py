from flask import Flask, render_template
from user_routes import user_bp
from admin_routes import admin_bp

app = Flask(__name__)

# 앱에다 블루프린트를 등록한다.
app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(admin_bp, url_prefix="/admin")

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

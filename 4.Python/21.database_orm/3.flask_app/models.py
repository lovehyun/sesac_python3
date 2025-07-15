from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 사용자 모델 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

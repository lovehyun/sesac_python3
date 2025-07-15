# pip install sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine('mysql:///')
engine = create_engine('sqlite:///example.db') # 상대경로로 설정하면 기본 디렉토리는 instacne 라는 폴더를 만들고 그 안에 생성됨
# engine = create_engine('sqlite:////tmp/example.db') # 절대경로 /tmp/example.db
# engine = create_engine('sqlite:///./example.db') # 절대경로 ./example.db (현재디렉토리)

# 베이스 클래스를 만들어서 객체랑 DB랑 연결
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'   # (옵셔널) DB 테이블명을 내가 지정해주고 싶을때
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# DB에게 테이블 생성하라고 시킴
Base.metadata.create_all(engine)

# 세션을 통해서 실제 DB와 CRUD를 함
Session = sessionmaker(bind=engine)
sess = Session()

# INSERT INTO users(name, age) VALUES('Alice', 30)
new_user = User(name="Alice", age=30)
sess.add(new_user)
sess.commit()

# SELECT * FROM users;
users = sess.query(User).all()
# print(users)
for user in users:
    print(user.id, user.name, user.age)

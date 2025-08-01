import sqlite3
import bcrypt

DB_FILENAME = 'users.db'

conn = sqlite3.connect(DB_FILENAME)
cur = conn.cursor()

# 테이블 생성
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    name TEXT NOT NULL
)
''')

def create_user(username, password, name):
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password, name) VALUES (?, ?, ?)",
                (username, hashed_pw, name))
    conn.commit()
    conn.close()

# 테스트 사용자 추가
create_user('user1', 'password1', 'UserName1')
create_user('user2', 'password2', 'UserName2')

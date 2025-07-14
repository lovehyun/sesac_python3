# pip install mysql-connector-python
# pip python-dotenv

from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()  # .env 파일의 환경변수 로드

# ▶ .env 예시
# MYSQL_HOST=localhost  # 실제서버의 IP주소 넣기
# MYSQL_PORT=3306  # 실제 서버의 Port 넣기
# MYSQL_USER=root   # 실제 서버의 계정 넣기
# MYSQL_PASSWORD=비밀번호   # 실제 서버의 비번 넣기
# MYSQL_DB=example   # 실제 DB 명 넣기

MYSQL_CONFIG = {
    "host":     os.getenv("MYSQL_HOST", "localhost"),
    "port":     int(os.getenv("MYSQL_PORT", 3306)), 
    "user":     os.getenv("MYSQL_USER", "root"), 
    "password": os.getenv("MYSQL_PASSWORD", ""), 
    "database": os.getenv("MYSQL_DB", "example"), 
    "autocommit": False,
}

# ──────────────────────────────────────────────
# DB 접속
def connect_db():
    return mysql.connector.connect(**MYSQL_CONFIG)

# 테이블 생성
def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id   INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age  INT          NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

# 데이터 삽입
def insert_user(name, age):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    cur.close()
    conn.close()

# 전체 조회
def get_users():
    conn = connect_db()
    cur = conn.cursor(dictionary=True)  # dict 형태 반환
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

# 이름으로 조회
def get_user_by_name(name):
    conn = connect_db()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM users WHERE name = %s", (name,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user

# 나이 업데이트
def update_user_age(name, new_age):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE users SET age = %s WHERE name = %s", (new_age, name))
    conn.commit()
    cur.close()
    conn.close()

# 삭제 함수들
def delete_user_by_name(name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE name = %s", (name,))
    conn.commit()
    cur.close()
    conn.close()

def delete_user_by_age(age):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE age = %s", (age,))
    conn.commit()
    cur.close()
    conn.close()

def delete_user_by_id(id_):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (id_,))
    conn.commit()
    cur.close()
    conn.close()

# pip install psycopg[binary]

from dotenv import load_dotenv
import os
import psycopg
from psycopg.rows import dict_row

load_dotenv()

PG_CONFIG = {
    "host":     os.getenv("PG_HOST", "localhost"),
    "port":     int(os.getenv("PG_PORT", 5432)),
    "user":     os.getenv("PG_USER", "postgres"),
    "password": os.getenv("PG_PASSWORD", ""),
    "dbname":   os.getenv("PG_DB", "example"),
    "autocommit": True,
    "row_factory": dict_row,  # dict 형태로 결과 반환
}

# DB 접속
def connect_db():
    return psycopg.connect(**PG_CONFIG)

# 테이블 생성
def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            age  INT NOT NULL
        )
    """)
    cur.close()
    conn.close()

# 데이터 삽입
def insert_user(name, age):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
    cur.close()
    conn.close()

# 전체 사용자 조회
def get_users():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

# 특정 사용자 조회
def get_user_by_name(name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = %s", (name,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user

# 사용자 나이 수정
def update_user_age(name, new_age):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE users SET age = %s WHERE name = %s", (new_age, name))
    cur.close()
    conn.close()

# 사용자 삭제
def delete_user_by_name(name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE name = %s", (name,))
    cur.close()
    conn.close()

def delete_user_by_age(age):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE age = %s", (age,))
    cur.close()
    conn.close()

def delete_user_by_id(id_):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (id_,))
    cur.close()
    conn.close()

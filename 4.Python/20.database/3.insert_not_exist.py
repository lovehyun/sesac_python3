import sqlite3

# DB 연결
conn = sqlite3.connect('example.db')

# 커서 객체 생성
cur = conn.cursor()

# ---------------------

# 데이터를 조회한다
cur.execute('SELECT COUNT(*) FROM users')
count = cur.fetchone()[0]

if count == 0: # 아무 사용자도 없으면?? 그때 삽입하기
    # 데이터 삽입
    cur.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
    cur.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Charlie', 40))
else:
    print('이미 데이터가 존재해서 더이상 삽입하지 않을것임.')
    print('현재 있는 사용자 데이터 갯수: ', count)

# --------------------

# 커밋하여 변경사항 저장
conn.commit()

# DB 연결을 종료
conn.close()

import sqlite3

# DB 연결
conn = sqlite3.connect('example.db')

# 커서 객체 생성
cur = conn.cursor()

# ---------------------

# 데이터 조회
cur.execute('SELECT * FROM users')

# 결과 가져오기 - 모든 행 다 가져오기 fetchall()
rows = cur.fetchall()
# print(rows)

for row in rows:
    print(row)

cur.execute('SELECT * FROM users')

print('-' * 10)
rows = cur.fetchone()
print(rows)

print('-' * 10)
cur.execute('SELECT COUNT(*) FROM users')
rows = cur.fetchall()  # 굳이 카운트는 하나인데, 다 달라고 해서 리스트에 담을거냐??
print(rows)
cur.execute('SELECT COUNT(*) FROM users')
rows = cur.fetchone()  # 하나를 잘 받아왔는데, 결과가 튜플임
print(rows)
cur.execute('SELECT COUNT(*) FROM users')
rows = cur.fetchone()[0]  # 하나를 잘 받아와서, 그 첫번째 항목만 가져오기
print(rows)

# --------------------

# 커밋하여 변경사항 저장
conn.commit()

# DB 연결을 종료
conn.close()

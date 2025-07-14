import sqlite3

# DB 연결
conn = sqlite3.connect('example.db')

# 커서 객체 생성
cur = conn.cursor()

# ---------------------

cur.execute('DELETE FROM users WHERE name="Alice"')

cur.execute('DELETE FROM users WHERE name=?', ('Bob', )) # 인자를 ('Bob') 이렇게만 표현하면, 이게 튜플인지, () 단일 인지를 말한건지, 그래서 (1 == 1) 이런 형태의 True/False를 계산하려는건지 모름.. 그래서 단일 인자일때도 튜플을 강제로 표현하기 위해서 빈 콤마를 넣어줌. ('값',)

# --------------------

# 커밋하여 변경사항 저장
conn.commit()

# DB 연결을 종료
conn.close()

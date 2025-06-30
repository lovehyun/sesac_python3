# https://docs.python.org/ko/3.10/library/datetime.html
# 빌트인 모듈 (built-in module) - 추가 설치 하지 않아도 바로 쓸 수 있음
import datetime as dt

# datetime.
# 모듈명.변수명
# 모듈명.클래스명.함수명()

print(dt.MINYEAR)
print(dt.MAXYEAR)

# YYYY-MM-DD HH:MM_SS.mmmmmm
# 현재 시간 가져오기
print(dt.datetime.now())
print(dt.datetime.now().strftime('%Y-%m-%d'))
print(dt.datetime.now().strftime('%H:%M:%S'))

# 내가 특정 날짜를 정해서 해당 시간값을 담아놓고 싶으면?
my_time = dt.datetime(2025, 6, 30, 10, 45, 00) # 현재 시간을 담은 datetime 이라는 개체
print(type(my_time))
print(my_time)

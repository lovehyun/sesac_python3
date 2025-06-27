# 파이썬은.. 변수라는걸 지정하는 키워드가 없음.. let, var, const
x = 5
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)

print(x % y) # 나머지 값
print(x ** y) # 거듭제곱 5 의 3승 (5^3)

str_x = "100"

# print (x + str_x) # 숫자와 문자는 더할 수 없음

int_x = int(str_x)  # 문자를 숫자(정수=integer) 로 변환
print("문자열 x:", str_x)
print("숫자 x:", int_x)

print (x + int_x)

# 비트 연산자
print("비트연산자 AND")
print(1 & 1) # 1
print(1 & 0) # 0
print(0 & 1) # 0
print(0 & 0) # 0
print("비트연산자 OR")
print(1 | 1) # 1
print(1 | 0) # 1
print(0 | 1) # 1
print(0 | 0) # 0

# 주의사항 (기계는 항상 2진수를 사용함..)
print(x & y) # 5 & 3 = ??? 1  : 101 & 011 = 1
print(x | y) # 101 | 011 = 111 = 7
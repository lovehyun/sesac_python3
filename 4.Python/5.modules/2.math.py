# https://docs.python.org/ko/3.10/library/math.html?highlight=math
# 기본 수학 연산을 하기 위한 빌트인 모듈

import math

print(math.pi)

# 원의 넓이를 구하려면??
# pi * radius ^ 2
radius = 5
area = math.pi * radius ** 2
area2 = math.pi * math.pow(radius, 2)
print(f"반지름이 {radius} 인 원의 넓이는 {area2:<10.2f} 입니다.") # .2f  소수 둘째짜리까지 표시

text = "Hi"
print(f"[{text:<10}]")
print(f"[{text:>10}]")
print(f"[{text:^10}]")

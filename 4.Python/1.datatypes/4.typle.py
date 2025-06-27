# 튜플 = 리스트와 동일하나, 데이터의 변경을 할 수 없음
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[-1])

# my_tuple[2] = 5 # 오류 발생.. 튜플 데이터는 수정 불가!!

my_list = list(my_tuple) # 튜플을 리스트로 변환 (복제본이 생김)
my_list[2] = 5
print(my_list)
print(my_tuple)

my_tuple2 = tuple(my_list)
# my_tuple2[2] = 10  # 튜플은 변경 불가!!

# 튜플안에 데이터를 여러개의 변수로 나누어 담을수 있음..
# 튜플 언패킹..
a, b, c = (1, 2, 3)
print(a)
print(b)
print(c)

a, _, c = (1, 2, 3)  # 받아와서 안쓸 변수를 파이썬의 관행으로 _ (밑줄) 사용
print(a)
# print(b)
print(c)

my_list = [1, 2, 3, 4, 5]
print(my_list)

print(len(my_list))
print(my_list[0])
print(my_list[1])
# print(mylist[5]) # 이게 JS에서는 undefined, 그 외 다른언어(python 포함) 에서는 오류
print(my_list[4])
print(my_list[-1]) # 거꾸로 갈 수 있음. 파이썬의 특징. 대부분의 다른 언어는 허용하지 않음.

# 리스트 슬라이싱
print(my_list[1:3]) # 1번 인덱스부터 3번째를 포함하기 전까지~ [1] [2] 만 나옴
print(my_list[0:5]) # 0번 인덱스부터 5를 포함하기 전까지~ 즉 [0 부터 4 까지 포함]

print(my_list[0:2])
print(my_list[2:4])

print(my_list[:2]) # 시작부터 2를 포함하기 전까지 [인덱스0~1 까지)
print(my_list[2:]) # 인덱스 2부터 끝까지 [인덱스2~])

# 리스트에 멤버 추가하기
print('-' * 10)
my_list.append(6)  # 기존의 리스트에 요소를 하나 끝에 추가하기
print(my_list)
my_list.insert(2, 10) # 인덱스2 위치 (즉 세번째) 에 숫자 10을 추가하겠음
print(my_list)

another_list = [7, 8, 9]
print(my_list)
print(another_list)

my_list.extend(another_list)
print(my_list)
print(another_list)

my_list.remove(10) # 나의 리스트에서 10 이라는 숫자를 삭제할거야
print(my_list)

my_list.pop(3) # 나의 리스트에서 인덱스3 에 있는 요소를 삭제할거야 (숫자 4가 있음)
print(my_list)

my_list.pop() # 인자를 안주면 마지막 요소 삭제
print(my_list)

my_list.clear() # 리스트 통째로 비우기
print(my_list)


# 리스트의 검색
print('-' * 10)
my_list = [1,2,3,4,5,3,2,1]

index_of_3 = my_list.index(3)  # 숫자3의 인덱스는 어디인가요??
print(index_of_3)

count_2 = my_list.count(2) # 2라는 숫자는 몇개나 있나요?
print(count_2)

print('--- 소팅전 ---')
print(my_list)
sorted_list = sorted(my_list)  # 이거는 인자를 받아서 반환하는 함수 (원본을 변경하지 않음)
print(sorted_list)
print('--- 소팅후 ---')
print(my_list)

print('-' * 10)
my_list.sort()  # 일부 함수는, 복제본을 만들어서 반환하는 애가 있고, 원본 데이터를 고치는 애가 있음.
# 뭐라고 정의 하지 않으면.. 오름차순 (작은거 -> 큰거순)
print(my_list)

my_list.sort(reverse=True) # 내림차순 (큰거 -> 작은거)
print(my_list)

my_list.reverse() # 현재 리스트를 역순으로 전환
print(my_list)

my_list2 = my_list.copy() # 리스트 복제
print(my_list2)

# 리스트 컴프리헨션 # 파이썬의 매~~~~우 큰 특징(장점)
# 리스트 안에 반복문 또는 조건문을 통해서, 리스트안에 채워질 요소를 정의할 수 있는 문법
numbers = [x        for x in range(10)] 
print(numbers)

numbers = [mynumber        for mynumber in range(5)] 
print(numbers)

numbers = [num for num in range(1,11)] # 1부터 10까지의 숫자를 만들어서, 이 리스트에 채우시오
print(numbers)

numbers = [num**2 for num in range(1,11)] # 1부터 10까지의 숫자를 만들어서, 그 제곱수로 채우시오
print(numbers)

numbers = [num       for num in range(1,11)      if num % 2 == 0] # 1부터 10까지의 숫자를 만들어서, 그중에 짝수로만 채우시오
print(numbers)


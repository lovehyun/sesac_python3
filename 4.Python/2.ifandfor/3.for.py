for i in range(5):
    print(i)
    
for i in [0, 1, 2, 3, 4]:
    print(i)
    
for i in range(1, 10):  # 끝값은 포함하지 않는다.
    print(i)
    
for i in range(1, 10, 2): # 1부터 10까지 2씩 건너뛴다
    print(i)

for i in range(1, 10, 3): # 1부터 10까지 3씩 건너뛴다
    print(i)

fruits = ['apple', 'banana', 'cherry']
for f in fruits:
    print(f)

for index, fruit in enumerate(fruits):
    print(index, fruit)

for i, f in enumerate(fruits):  # 지금 시대는 이거보다는 위에처럼 길고 설명/이해가 좋은 변수를 쓸 것
    print(i, f)

str = "Hello, World!"
for char in str:
    print(char)
    
# 위 문장에서 o 의 갯수를 구하시오.
count_o = 0
for char in str:
    if char == 'o':
        count_o += 1   # count_o = count_o + 1
print(f'{str} 문장내의 o의 갯수는 {count_o} 개 입니다.')

count_l = 0
for char in str:
    if char == 'l':
        count_l += 1
print(f'{str} 문장내의 l의 갯수는 {count_l} 개 입니다.')

numbers = [3, 7, 2, 9, 1, 4, 5, 8, 6]

def find_max(numbers):
    # 위 목록에서 가장 큰 수를 반환하시오
    # for 와 if 를 사용해서....
    max_num = 0   # 0 을 초기값으로 하면, 어떤 문제가 있을까??
    # max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    
    return max_num

print(find_max(numbers))

print(max(numbers))  # 내장 함수 사용한것

numbers.sort(reverse=True)  # 치트키 사용한것..
print(numbers[0])


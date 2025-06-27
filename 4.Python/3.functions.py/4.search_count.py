# numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
numbers = list(range(1, 1000001))

# 원하는 숫자를 찾았으면, 해당 인덱스를 반환하고, 없으면 -1 을 반환하시오
def linear_search(numbers, target):
    count = 0
    for i in range(len(numbers)):
        count += 1
        if numbers[i] == target:
            print("선형탐색에서의 비교횟수: ", count)
            return i
        
    return -1

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    count = 0
    
    while left <= right:
        mid = (left + right) // 2 # 나머지를 제외한 몫만 구하는...
        count += 1
        if numbers[mid] == target:
            print("이진탐색에서의 비교횟수: ", count)
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

target = 1000000
print(linear_search(numbers, target))
print(binary_search(numbers, target))

numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 원하는 숫자를 찾았으면, 해당 인덱스를 반환하고, 없으면 -1 을 반환하시오
def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
        
    return -1

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    
    while left <= right:
        mid = (left + right) // 2 # 나머지를 제외한 몫만 구하는...
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

target = 17
print(linear_search(numbers, target))
print(binary_search(numbers, target))

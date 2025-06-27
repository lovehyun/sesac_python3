def remove_duplicate(number): # legacy 한 c 스타일의 코드...
    # 구현하기
    # 1. 목록을 순회한다
    # 2. 내가 한번도 본적이 없는 숫자면 반환 리스트에 담는다
    unique_numbers = []
    for num in numbers:
        seen_num = False
        for prev_num in unique_numbers:
            if num == prev_num:
                seen_num = True
                
        if seen_num == False:
            unique_numbers.append(num)
    
    return unique_numbers


def remove_duplicate2(number):  # 파이썬 스러운 코드...
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    return unique_numbers


def remove_duplicate3(number):  # 더 modern 한 python 스러운 코드...
    return list(set(number))

numbers = [1,2,3,4,3,2,1,5,6,7,6,5]
print(remove_duplicate(numbers))
print(remove_duplicate2(numbers))
print(remove_duplicate3(numbers))

def square_root(number):
    if (number < 0):
        print("음수는 스퀘어루트를 구할수 없습니다")
        return None
    
    return number ** 0.5

def square_root2(number):
    if (number < 0):
        raise ValueError("음수의 제곱근은 계산 할 수 없습니다.")
    
    return number ** 0.5

print(square_root(25))
print(square_root(10))
print(square_root(1))
print(square_root(-25))

try:
    print(square_root2(-25))
except ValueError as e:
    print(e)

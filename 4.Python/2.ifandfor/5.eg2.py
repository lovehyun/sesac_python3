# 데이터베이스
users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Charlie", "age": 40, "location": "Suwon", "car": "Audi"},
    {"name": "Bob", "age": 40, "location": "Jeju", "car": "Mercedes"},
]

# 사용자 이름을 기반으로, 해당 사용자 정보를 가져오는 코드 구현하기

# for u in users:
    # print(u)

def find_user(name):
    for u in users:
        if u["name"] == name:
            return u

def find_users(name):
    result = []
    for u in users:
        if u["name"] == name:
            result.append(u)
    return result

def find_users_caseinsensitive(name):
    result = []
    for u in users:
        if u["name"].lower() == name.lower(): # DB 내용도, 사용자의 입력도 모두다 소문자로 바꿔서 비교
            result.append(u)
    return result
        
# print(find_user("Alice"))
# print(find_user("Charlie"))
# print(find_user("David"))
# print(find_user("Bob"))
# print(find_users("Bob"))
# print(find_users_caseinsensitive("bob"))
# print(find_users_caseinsensitive("BOB"))

def find_user2(name, age):
    for u in users:
        # if u["name"] == name & u["age"] == age:   # 연산자 우선순위로 ()가 필수임
        # if (u["name"] == name) & (u["age"] == age):   # 이건 잘 동작함
        if u["name"] == name and u["age"] == age:    # 이게 가장 파이썬 스러운 표현법
            return u

print(find_user2('Alice', 25))
print(find_user2('Bob', 40))

print('--- find_user3 할차례 ---')
def find_user3(name=None, age=None):
    result = []
    
    for u in users:
        if name:
            if u["name"] == name:
                if age:
                    if u["age"] == age:
                        # 둘다 매치된 상황
                        result.append(u)
                else:
                    # 이름은 매치되고, 나이는 신경 안쓰는 경우
                    result.append(u)
        elif age:
            # 이름이 없고, 나이만 있는 경우
            if u["age"] == age:
                result.append(u)
        else:
            result.append(u)
            
    return result

print(find_user3(name='Bob'))
print(find_user3(age=40))
print(find_user3('Bob', 40))
print(find_user3(age=40, name='Bob'))

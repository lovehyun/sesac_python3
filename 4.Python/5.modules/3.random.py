# https://docs.python.org/ko/3.10/library/random.html?highlight=random#module-random
# 무작위 숫자 만들기..

# import random as rand
import random

print("랜덤 숫자: ", random.randint(1, 100)) # 1부터 100까지의 양수를 다 포함하는 랜덤 숫자를 생성

# 주사위 던지기 구현
def roll_dice():
    # number = random.randint(1, 6)
    # return number
    return random.randint(1, 6)

print(f"주사위 던진 결과: {roll_dice()}")

# 이 주사위를 100번 던져보고, 1000도 해보고, 10000번도 던져서... 각 숫자가 나올 확율을 출력해보시오
# 1이 나온 횟수: ooo번, 확율: 00.00%
# 2이 나온 횟수: ooo번, 확율: 00.00%
# 3이 나온 횟수: ooo번, 확율: 00.00%
# 4이 나온 횟수: ooo번, 확율: 00.00%
# 5이 나온 횟수: ooo번, 확율: 00.00%
# 6이 나온 횟수: ooo번, 확율: 00.00%

# for 문으로 반복해서 결과를 취합해서, 위 내용을 출력하시오
#         1, 2, 3, 4, 5, 6
counts = [0, 0, 0, 0, 0, 0]
def roll_dices(numbers):
    for i in range(numbers):
        result = roll_dice()
        # 하나하나 개별 숫자를 6번 비교해서 인덱스를 올려도 무방함
        # if result == 1:
        #     counts[0] += 1
        # elif result == 2:
        #     counts[1] += 1
        # elif result == 3:
        #     counts[2] += 1
        # 등등등...
        
        # 짧은게 좋은건데, 일주일 후에 봐서 이해가 안되면?? 복잡한 코드가 된것..
        counts[result - 1] += 1
     
roll_dices(100_000)
for i in range(6):
    print(f"{i+1} 이 나온 횟수: {counts[i]}: 확율: {counts[i] / sum(counts)}")


# 위에 보다 좀 더 modern 한 파이썬 스타일의 코드

# 딕셔너리 라는 자료구조이고, key:value 라는 형태로 정의해서...
# 여기서의 키는 주사위 숫자 자신을 바로 의미함
# counts2 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
counts2 = {i: 0           for i in range(1, 7)}
print(counts2)

def roll_dices2(numbers):
    for _ in range(numbers):
        result = roll_dice()
        counts2[result] += 1

trial = 100_000
roll_dices2(trial)
print(counts2)

for dice_num, dice_count in counts2.items():
    # print(dice_num, dice_count)
    print(f"주사위 수 {dice_num} 이 나온 횟수는 {dice_count} 입니다. 확율은: {dice_count / trial:.2%}")

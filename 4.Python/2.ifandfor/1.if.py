score = 80
if score >= 90:
    print("A학점")
elif score >= 80:   # 다른 많은 언어는 else if
    print("B학점")
elif score >= 80:
    print("C학점")
else:
    print("F학점")


def getGrade(score):
    if score >= 90:
        grade = "A학점"
    elif score >= 80:   # 다른 많은 언어는 else if
        grade = "B학점"
    elif score >= 80:
        grade = "C학점"
    else:
        grade = "F학점"
        
    return grade

john = getGrade(70)
print("John의 학점: ", john)

jane = getGrade(95)
print("jane 학점: ", jane)

# 내장함수 (built-in functions)
# 사용자로부터 입력받기
user = input("점수를 입력하시오: ")
userScore = getGrade(int(user))
print("사용자의 점수는:", userScore, "입니다")

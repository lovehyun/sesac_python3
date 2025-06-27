def getGrade(score):
    scoreInt = int(score)
    
    if scoreInt >= 90:
        grade = "A학점"
    elif scoreInt >= 80:   # 다른 많은 언어는 else if
        grade = "B학점"
    elif scoreInt >= 80:
        grade = "C학점"
    else:
        grade = "F학점"
        
    return grade

name = input("이름을 입력하시오:")
score = input("점수를 입력하시오:")
grade = getGrade(score)
print(f"학생 {name} 의 성적은 {grade} 입니다.")

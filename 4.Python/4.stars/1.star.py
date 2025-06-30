# print('*')
# print('**')
# print('***')
# print('****')
# print('*****')

def draw_ltriangle(lines):
    for i in range(1,lines+1):
        print('*' * i)

def draw_rtriangle(lines):
    n = lines
    for i in range(1, lines+1):
        print(' ' * (n-i), end="") # 공백그리기
        print('*' * i) # 별 그리기
        # print(' ' * (n-i) + '*' * i)

def draw_iltriangle(lines):
    for i in range (5, 0, -1):
        print('*' * i) # 별 그리기

def draw_irtriangle(lines):
    n = lines
    for i in range (5, 0, -1):
        print(' ' * (n-i) + '*' * i) # 별 그리기
        
print('-- ltriangle --')
draw_ltriangle(5)
print('-- rtriangle --')
draw_rtriangle(5)
print('-- iltriangle --')
draw_iltriangle(5)  # 역삼각형 inverse
print('-- irtriangle --')
draw_irtriangle(5)

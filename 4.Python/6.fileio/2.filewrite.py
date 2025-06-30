file_path = "test.txt"

# 파일을 읽으때의 "모드"
# r = read, w = write(새로쓰기), a = append(이어서쓰기)
with open(file_path, "w", encoding='utf-8') as file:
    file.write("Hello!\n\n")  # \n 뉴라인 - 줄바꿈 캐릭터
    file.write("안녕!")
    file.write("\n바이!")

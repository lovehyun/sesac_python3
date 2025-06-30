file_path = "file.txt"
file = open(file_path, "r")  # file 을 file descriptor 라고 부름 FD

contents = file.read()

file.close()

# 파일을 연다 (열때 해당 파일을 가르키는 FD를 가져온다)
# FD를 통해서 파일을 읽고/쓰고 함
# 파일을 닫는다

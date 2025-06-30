import os

my_dir = 'sesac1234'

# 디렉토리 안에 파일"만" 읽어오기
for filename in os.listdir(my_dir):
    file_path = os.path.join(my_dir, filename)
    if (os.path.isfile(file_path)):
        print(filename)

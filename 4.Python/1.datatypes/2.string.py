str = "Hello, World!"
str2 = "  Welcome to sesac class  "
print(str)

# 라이브러리 함수들로 만들어 놨음.. 이걸 잘~~ 알아야함...
print(str.lower())
print(str.upper())
print(str.capitalize()) # 문장의 시작만 대문자로...
print(str2.title())  # 문장의 단어 단어마다 대문자로...
print(str2.strip())  # 앞뒤 불필요한 공백 제거
print(str2.lstrip())
print(str2.rstrip())
print(str.split()) # 문장을 단어 단위로 짜른다
print(str2.split())

words = str2.split()
print(words[0])
print(words[2])
print(words[2].upper())
print(",".join(words))
print(" ".join(words))
print("-".join(words))

print(str.startswith("Hello"))
print(str.startswith("hello"))

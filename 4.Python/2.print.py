name = "Alice"
print(name)
print("Hello,", name) # 인자(argument) 로 받으면 띄어쓰기 자동
print("Hello," + name) # 덧셈 연산 은 띄어쓰기 안해줌
print("Hello," + name + "!!")

print("Hello, {}!!".format(name))
print("Hello, {}!! {}??".format(name, name))

name1 = "Bob"
name2 = "Charlie"
print("Hello, {}!! {}??".format(name1, name2))
print("Hello, {0}!! {1}??".format(name1, name2))
print("Hello, {1}!! {0}??".format(name1, name2))

print("Hello, %s!!" % name)  # %s 는 문자열을 출력하는곳이다.
print("Hello, %s!! %s??" % (name1, name2))

# 결론적으로, 위의 다양한 것들을 거쳐서... 지금 가장 많이 쓰는건
# f-스트링 표기법 (JS에서 `${변수}` 백틱안에 포멧팅하듯이...)
print(f"Hello, {name}!!")
print(f"Hello, {name1}!! {name2}!!")

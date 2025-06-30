numbers = [1, 2, 3, 4, 5]

first_value = None
last_value = None

try:
    first_value = numbers[0]
    print(f"첫번째 숫자는 {first_value} 입니다.")

    # last_value = numbers[5]     # 크래쉬 발생!!
    last_value = numbers[4]
    print(f"마지막 숫자는 {last_value} 입니다.")
except IndexError:
    print("숫자를 잘못 참조하고 있습니다. 첫번째 또는 마지막 인덱스가 잘못 되었습니다.")


if first_value and last_value:
    diff = last_value - first_value
    print(f"두 수의 차이는 {diff} 입니다.")
else:
    print(f"알 수 없는 오류입니다???")

class Person:
    # 초중급 에서도 필수
    def __init__(self, name, age):
        self.name = name  # 속성 (Attribute) - 개별 데이터를 저장하는 공간
        self.age = age   # 속성 (Attribute)
    
    # 초중급 까지는 잘 안씀
    def __str__(self):  # 이 객체를 사람들이 보기 좋게 표현하는 함수
        return f"Person(name={self.name}, age={self.age})"

    # 초중급 까지는 전혀 안씀
    def __eq__(self, other):  # 나와(이객체) 와 다른 객체를 비교할때의 조건
        return self.name == other.name and self.age == other.age
        
    def greet(self):   # 메소드 (Method - 객체 함수)
        print(f"안녕하세요, 저는 {self.name} 입니다.")

    def ride_car(self):  # 메소드 (Method - 객체 함수)
        print(f"자동차를 탑니다")

person1 = Person("김철수", 30)
person2 = Person("홍길동", 25)
person3 = Person("아무개", 22)
person4 = Person("김철수", 30)

person1.greet()
person1.ride_car()

person2.greet()
person2.ride_car()

person3.greet()

print(person1)
print(person1 == person2)
print(person1 == person3)
print(person1 == person1)
print(person1 == person4)

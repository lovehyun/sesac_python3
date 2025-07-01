from person import Person

class Employee(Person):  # 또 상속~
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self._company = company
        
    def greet(self):  # 사람의 인사대신, 나만의 인사를 할거야. 메소드 오버라이딩(over-riding)
        print(f"저는 {self._company} 에서 일하는 {self.name} 입니다.")
        
    def work(self):
        print(f"직원 {self.name} 은/는 {self._company} 에서 일하는 중입니다.")

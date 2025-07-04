from abc import ABC, abstractmethod

# 추상 클래스 - 필수로 구현해야 하는 함수를 지정 하였음
class Displayable(ABC):
    @abstractmethod
    def display(self):
        pass

class User(Displayable):
    def display(self):
        print("사용자 객체 처리")

class Store(Displayable):
    def display(self):
        print("상점 객체 처리")

class Item(Displayable):
    def display(self):
        print("아이템 객체 처리")
        
class Order(Displayable):
    # def display_order(self):
    def display(self):                # 이걸 강제로 하도록 만듦
        print("주문 객체 처리")

# 내가 출력해줄게.. 근데, 디테일은 모르겠어.. 그건 니가 해... 어디에?? display() 라는 함수로...
# 그러나, 그렇게 안지켜도 강제화가 안되어 있는...
class DisplayData:
    def __init__(self, data):
        data.display()
    
DisplayData(User())
DisplayData(Store())
DisplayData(Item())
DisplayData(Order())   # 런타임 오류 형태로 발생.. 그래서 좋지 않음... 컴파일 타임에 이런게 잡혀야 함.. (그래야 예방 가능)

# 이렇게 밑에서 개별적으로 호출하지 않고, 위에처럼.. 중간 중계자를 통해서 처리하는 구조가 OOP 적인 설계...
User().display()
Store().display()

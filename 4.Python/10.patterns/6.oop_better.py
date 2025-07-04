from abc import ABC, abstractmethod

# 추상 클래스 - 필수로 구현해야 하는 함수를 지정 하였음
class Displayable(ABC):
    registry = {}
    
    def __init_subclass__(cls, **kwargs):    # 나를 상속 받은 애들이 자동으로 실행하게 되는 함수
        super().__init_subclass__(**kwargs)
        Displayable.registry[cls] = cls  # 그래서 나를 상속해간 놈들이 누군지 registry 에 기록함
    
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

class OrderItem():
    def display(self):
        print("아이템 객체 처리")
        
# 내가 출력해줄게.. 근데, 디테일은 모르겠어.. 그건 니가 해... 어디에?? display() 라는 함수로...
# 그러나, 그렇게 안지켜도 강제화가 안되어 있는...
class DisplayData:
    def __init__(self, data):
        handler = Displayable.registry.get(type(data))
        if handler:
            data.display()
        else:
            print("지원하지 않는 타입입니다")
    
DisplayData(User())
DisplayData(Store())
DisplayData(Item())
DisplayData(Order())
DisplayData(OrderItem())  # 제대로 상속받아서 규칙에 맞게 설정한 애들만 동작 가능함.

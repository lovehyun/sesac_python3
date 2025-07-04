class User:
    pass

class Store:
    pass

class Item:
    pass

class DisplayData:
    def __init__(self, data):
        self.handlers = {
            User: self.display_user,
            Store: self.display_store,
            Item: self.display_item
            # 새로운 타입이 추가되면 여기에 계속 추가...
        }
        handler = self.handlers.get(type(data), self.unsupported_type)  # .get() 은 있으면 반환, 없으면 기본값을 두번째 인자로..
        handler(data)
    
    def display_user(self, data):
        print(f"사용자 정보: {data}")
        
    def display_store(self, data):
        print(f"상점 정보: {data}")
        
    def display_item(self, data):
        print(f"아이템 정보: {data}")
        
    def unsupported_type(self, data):
        print("지원하지 않는 타입입니다.")
            
DisplayData(User())
DisplayData(Store())
DisplayData(Item())
DisplayData(123)

class DisplayData:
    def __init__(self, data):
        self.handlers = {
            str: self.display_str,
            list: self.display_list,
            dict: self.display_dict
            # 새로운 타입이 추가되면 여기에 계속 추가...
        }
        handler = self.handlers.get(type(data), self.unsupported_type)  # .get() 은 있으면 반환, 없으면 기본값을 두번째 인자로..
        handler(data)
    
    def display_str(self, data):
        print(f"문자열: {data}")
        
    def display_list(self, data):
        print(f"리스트: {data}")
        
    def display_dict(self, data):
        print(f"딕셔너리: {data}")
        
    def unsupported_type(self, data):
        print("지원하지 않는 타입입니다.")
            
DisplayData("hello")
DisplayData([1, 2, 3])
DisplayData({"a":1, "b":2})
DisplayData(123)

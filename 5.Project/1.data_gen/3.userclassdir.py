from generators.user_generator import UserGenerator

class DisplayData(UserGenerator):
    def print_data(self, count):
        data = self.generate_user(count)
        for name, birthdate, gender, address in data:
            print(f"Name: {name}\nBirthdate: {birthdate}\nGender: {gender}\nAddress: {address}\n")

# 최종 실행
my_data = DisplayData()
my_data.print_data(100)

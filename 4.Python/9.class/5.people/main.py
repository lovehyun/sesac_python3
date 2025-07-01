# import person
from person import Person
from student import Student
from employee import Employee

alice = Person("Alice", 23)
bob = Person("Bob", 24)
tom = Student("Tom", 20, "S12345678")
charlie = Employee("Charlie", 30, "Samsung")

alice.greet()
bob.greet()
bob.name = "BOB"
bob.greet()

tom.greet()
tom.study()

charlie.greet()
charlie.work()

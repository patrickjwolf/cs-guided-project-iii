class MyFirstClass:
    pass
  
  
my_first_instance = MyFirstClass()
my_second_instance = MyFirstClass()

print(my_first_instance)
print(my_second_instance)
print(MyFirstClass)




class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

def __str__(self):
    return f"This student's name is {self.last_name}, {self.first_name}"

me = Student("Patrick", "Wolf")
print(me)

you = Student("Sam", "Fry")
print(you)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "Hello"
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

my_point = Point(3, 5)
print(my_point)




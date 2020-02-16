class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
    def show(self):
        print(self.name, self.rollno)

s1 = Student('Navin', 2)
s2 = Student('Jenny', 3)
s1.show()

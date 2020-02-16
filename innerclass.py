class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.CPU = 'i5'
            self.RAM = 8

        def show(self):
            print(self.brand, self.CPU, self.RAM)

s1 = Student('Navin', 2)
s2 = Student('Jenny', 3)
s1.show()

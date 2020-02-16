class Student():
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def add(self):
        print(self.value1 + self.value2)

    def sub(self):
        print(self.value1 - self.value2)

    def mul(self):
        print(self.value1 * self.value2)

feed = Student(
    value1=int(input("Enter the first value  :")),
    value2=int(input("Enter the second value :"))
)

print("The addition of the two values is   :", end=" ")
Student.add(feed)
print("The difference of the two values is :", end=" ")
Student.sub(feed)
print("The product of the two values is    :", end=" ")
Student.mul(feed)

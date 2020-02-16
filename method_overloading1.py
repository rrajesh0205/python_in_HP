class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a, b):
        c = a + b
        return c

s1 = Student(58, 69)
print(s1.sum(5, 9))

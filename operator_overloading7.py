class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{}, {}'.format(self.m1, self.m2)

s1 = Student(58, 69)
s2 = Student(69, 65)

print(s1)
print(s2)
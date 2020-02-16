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


s1 = Student(59, 65)
s2 = Student(60, 65)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

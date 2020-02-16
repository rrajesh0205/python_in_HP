class Student():
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __sub__(self, other):
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        s3 = Student(m1, m2)
        return s3

feed = Student(
    m1=int(input("Enter the first value  :")),
    m2=int(input("Enter the second value :"))
)

print("The difference between the first value and the second is:", end=" ")
print(feed.m1 - feed.m2)

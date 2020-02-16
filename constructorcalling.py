class A:
    def __init__(self):
        print("in A Init")
    def feature1(self):
        print("This is feature1")
    def feature2(self):
        print("This is feature2")

class B(A):
    def feature3(self):
        print("This is feature3")
    def feature4(self):
        print("This is feature4")

a1 = A()

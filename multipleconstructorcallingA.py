class A:
    def __init__(self):
        print("in A Init")
    def feature1(self):
        print("This is feature1")
    def feature2(self):
        print("This is feature2")

class B:
    def __init__(self):
        print("in B Init")
    def feature3(self):
        print("This is feature3")
    def feature4(self):
        print("This is feature4")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("in C Init")
    def feature5(self):
        print("This is feature5")


a1 = C()

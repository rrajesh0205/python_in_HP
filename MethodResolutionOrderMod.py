class A:
    def __init__(self):
        print("in A Init")
    def feature1(self):
        print("This is feature 1 in class A and is Working")
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
    def feat(self):
        super().feature2()
    def feature5(self):
        print("This is feature5")


a1 = C()
a1.feat()

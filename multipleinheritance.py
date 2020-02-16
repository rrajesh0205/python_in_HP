class A:
    def feature1(self):
        print("This is feature1, in class A")
    def feature2(self):
        print("This is feature2, in class A")

class B:
    def feature3(self):
        print("This is feature3, in class B")
    def feature4(self):
        print("This is feature4, in class B")

class C(A,B):
    def feature5(self):
        print("This is feature5, in class C(B) which is C(A,B)")

a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature3()
b1.feature4()

c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()

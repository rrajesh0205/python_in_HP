class A:
    pass

class B:
    def show(self):
        print("This has been called from Class B")

class C(A, B):
    pass

a1 = C()
a1.show()
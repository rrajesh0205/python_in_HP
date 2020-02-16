class A:
    def show(self):
        print("This has been called from Class A")

class B(A):
    pass

a1 = B()
a1.show()
class A:
    def show(self):
        print("This has been called from Class A")

class B(A):
    def show(self):
        print("This has been called from Class B")

# Note that there is a same attribute show in A but it prints calls only from B Class and not from the Class A
# And this is method overriding. It overrides.

a1 = B()
a1.show()
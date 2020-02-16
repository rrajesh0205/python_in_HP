class computer:
    def __init__(self):
        self.name="Navin"
        self.age=28
        
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
c1 = computer()
c1.age = 29
c2 = computer()
if c1.compare(c2):
    print("They are of the same age")
else:
    print("The age is different")
print (c1.name)
print (c2.name)


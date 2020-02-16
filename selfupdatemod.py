class Computer:
    def __init__(self):
        self.name = "Navin"
        self.age = 28

    def update(self):
        self.age = 30

c1 = Computer()
c2 = Computer()

c2.name = "Rashi"
c2.age = 12

c2.update()

print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)

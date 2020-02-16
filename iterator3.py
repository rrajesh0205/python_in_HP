class TopTen:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        val = self.num
        self.num += 1
        return val

values = TopTen()
for i in values:
    print(i)

def TopTen():
    yield 5
values = TopTen()
print(values.__next__())
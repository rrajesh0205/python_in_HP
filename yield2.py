def TopTen():
    yield 1
    yield 2
    yield 3
    yield 4
values = TopTen()
print(values.__next__())
print(values.__next__())
for i in values:
    print(i)
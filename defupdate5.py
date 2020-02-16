def update(list):
    print(id(list))
    list[1] = 25
    print(id(list))
    print("x ", list)
list = [10, 20, 30]
print(id(list))
update(list)
print("list", list)
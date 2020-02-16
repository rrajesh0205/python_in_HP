a = 10
def something():
    a = 15
    print("Inside function / Local", a)
something()
print("Outside function / Global", a)
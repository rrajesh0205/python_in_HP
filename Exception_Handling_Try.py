a = 5
b = 0
try:
    print("Resource is now open")
    print(a/b)
except Exception as e:
    print("Hey, you cannot divide a Number by Zero", e)
    print("Resource is now Closed")

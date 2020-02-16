a = 5
b = 2
try:
    print("Resource is now open")
    print(a/b)
    k = int(input("Enter a Number"))
    print(k)
except ZeroDivisionError as e:
    print("Hey, you cannot divide a Number by Zero", e)
except ValueError as e:
    print("Invalid Input, Please enter Integers...")
except Exception as e:
    print("Something went wrong...")
finally:
    print("Resource is now Closed")
    

x = int(input("Enter any first number"))
y = int(input("Enter any second number"))
z = int(input("Enter any third number"))
if x > y > z:
    print("The user input of the numbers are....")
    print(x)
    print(y)
    print(z)
    print(x,"is the greatest of the three numbers")
else:
    if y > z:
        print("The user input of the numbers are")
        print(x)
        print(y)
        print(z)
        print(y, "is the greatest of the three numbers")
    else:
        print("The user input of the numbers are")
        print(x)
        print(y)
        print(z)
        print(z, "is the greatest of the three numbers")
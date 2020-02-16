def multiply(x, y):
    c = x * y
    return c


x = int(input("Enter the first value to multiply..."))
y = int(input("Enter the second value to multiply..."))
result = multiply(x, y)
print()
print("The Result of", x,"*", y, "is = ", result)

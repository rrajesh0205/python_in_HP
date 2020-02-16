def count(numberList):
    even = 0
    odd = 0
    for i in numberList:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

numberList = []
n = int(input("Enter the list size : "))
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = int(input())
    numberList.append(item)
print("User List is ", numberList)

even, odd = count(numberList)
print("Even : {} and Odd : {}" .format(even,odd))



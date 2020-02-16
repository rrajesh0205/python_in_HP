position = -1
def search(numberList,n):
    i = 0
    for i in range(len(numberList)):
        if numberList[i] == n:
            globals()['position'] = i
            return True
        i = i + 1
    return False

numberList = []
nl = int(input("Enter the list size : "))
for i in range(0, nl):
    print("Enter number at location", i, ":", end=" ")
    item = int(input())
    numberList.append(item)
print("User List is ", numberList)

n = int(input("Enter the number you need to check in the list : "))
if search(numberList,n):
    print("I Found", n, "in the List at Position", position+1)
else:
    print("Sorry", n, "is not in the List")

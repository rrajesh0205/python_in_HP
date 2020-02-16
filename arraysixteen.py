from array import*
arr = array('i',[ ])
n = int(input("Enter the length of the array"))
for i in range(n):
    x = int(input("Enter the value"))
    arr.append(x)
print(arr)

# manual method to reverse a given or inputted array.
print("The array has been reversed")
print("Here's the reversed array:", end=" ")

for i in range(len(arr), 0, -1):
    print (arr[i-1], end=" ")


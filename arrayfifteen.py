from array import*
arr = array('i',[ ])
n = int(input("Enter the length of the array"))
for i in range(n):
    x = int(input("Enter the value"))
    arr.append(x)
print(arr)

# manual method to find the index of a given or inputted array.

val = int(input("Enter the value for search and remove..."))
k = 0
for e in arr:
    if e == val:
        arr.remove(val)
        print("The index number",k," has been removed")
        print("The new array is",arr)
        break
    k += 1



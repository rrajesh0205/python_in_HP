position = -1
def search(list,n):
    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u) // 2
        
        if list[mid] == n:
            globals()['position'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid +1
            else:
                u = mid -1
    return False

list = []
nl = int(input("Enter the list size : "))
for i in range(0, nl):
    print("Enter number at location", i, ":", end=" ")
    item = int(input())
    list.append(item)
    # why this list.sort().
    # Binary Search will only work if the list is sorted.
    
    list.sort() 
print("User List is ", list)

n = int(input("Enter the number you need to check in the list : "))
    
if search(list,n):
    print("Entered number", n, "is in the List", position+1)
else:
    print("Sorry", n, "is not in the List")

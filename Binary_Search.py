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
    
list = [4, 7, 8, 12, 45, 99, 102, 105]

n = 45
if search(list,n):
    print("I Found", n, "in the List", position+1)
else:
    print("Sorry", n, "is not in the List")

def sort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i,len(nums)):
            if nums[j] < nums [minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

nums = []
nl = int(input("Enter the list size : "))
for i in range(0, nl):
    print("Enter number at location", i, ":", end=" ")
    item = int(input())
    nums.append(item)

print("User List is ", nums)

sort(nums)
print(nums)

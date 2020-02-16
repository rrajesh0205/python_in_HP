def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = []
nl = int(input("Enter the list size : "))
for i in range(0, nl):
    print("Enter number at location", i, ":", end=" ")
    item = int(input())
    nums.append(item)
print("The User List is ...: ", nums)


sort(nums)
print("The sorted list is .: ", nums)

nums = [7,8,9,5]
it = iter(nums)
print(it.__next__())
print(it.__next__())
print(next(it))
for i in nums:
    print(i)
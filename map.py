def update(n):
    return n+2
nums = [3,2,6,8,4,6,2,9]
even = list(filter(lambda n : n % 2 ==0, nums))
doubles = list(map(update,even))
print("Even number from list:", even)
print("Adding Two with even :", doubles)
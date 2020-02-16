from functools import reduce
nums = [3,2,6,8,4,6,2,9]
even = list(filter(lambda n : n % 2 ==0, nums))
doubles = list(map(lambda n : n * 2, even))
sum = reduce(lambda a, b: a + b, doubles)
print("Even number from list  :", even)
print("Adding Two with even   :", doubles)
print("Adding all the Numbers :", sum)
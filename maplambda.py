nums = [3,2,6,8,4,6,2,9]
even = list(filter(lambda n : n % 2 ==0, nums))
doubles = list(map(lambda n : n * 2, even))
print("Even Numbers from the list ....", even)
print("Printing Even multiplied by two", doubles)
def is_even(n):
    return n % 2 == 0
nums = [3,2,6,8,4,6,2,9]
even = list(filter(is_even,nums))
print(even)
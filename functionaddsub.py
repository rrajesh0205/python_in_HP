def add_sub(x: object, y: object) -> object:
    c = x + y
    d = x - y
    return c, d


result1, result2 = add_sub(5, 4)
print(result1, result2)

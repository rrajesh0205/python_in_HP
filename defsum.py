def sum(a, *b):
    c = a
    for i in b:
        c = c + i
    print(c)
sum(5, 6, 34, 78)
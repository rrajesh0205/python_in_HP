n = int(input("Enter the number of items in Fibonacci series..."))
def fib(n):
    a = 0
    b = 1
    if n < 0:
        print("This is a invalid number...")
        print("Fibonacci series starts from 0 ...")

    else:
        if n == 0:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(1,n):
                c = a + b
                a = b
                b = c
                print(c)
fib(n)
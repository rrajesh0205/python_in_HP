# to take input from the use
num = int(input("Enter the number to check whether it is prime or not"))
# prime numbers are greater than 1
if num>1:
    # check for factors
    for i in range(2,num):
        if num % i==0:
            print(num, "is not a Prime Number")
            print(i, "times", num//i, "is", num)
            break
    else:
        print(num, "is a Prime Number")
# if the inputted number is less than
# or equal to 1, then it is not prime
else:
    print(num,"is not a Prime Number")

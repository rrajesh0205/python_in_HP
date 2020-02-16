av=20
print("The available candies in the vending machine is", av)
x = int(input("How many candies do you need?"))
i=1
while i<=x:
    if i>av:
        break
    print("Candy")
    i=i+1
print("Bye")
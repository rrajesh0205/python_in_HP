x=int (input("enter the number to find the greater one"))
y=int (input("enter the number to find the greater one"))
z=int (input("enter the number to find the greater one"))
if x>y>z:
    print("the number",x,"is greater")
else:
    if y>z:
        print("the number",y,"is greater")
    else:
        print("the number",z,"is greater")
# This code calculates the data from other files sumcal.py subcal.py mulcal.py and divcal.py
# Refer to sumcal.py subcal.py mulcal.py and divcal.py for the calculations of this code

from sumcal import *
from subcal import *
from mulcal import *
from divcal import *

a = int(input("Enter the first number.."))
b = int(input("Enter the second number."))
c = add(a, b)
d = sub(a, b)
e = multi(a, b)
f = div(a, b)
print()

print("The Results are as follows......")
print()
print("The addition of...", a, "and", b, "is: ", c)
print("The subtraction of", a, "and", b, "is: ", d)
print("The product ......", a, "and", b, "is: ", e)
print("The division......", a, "and", b, "is: ", f)
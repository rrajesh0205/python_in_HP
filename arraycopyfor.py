# add two arrays using for loop

from numpy import *
arr1 = array([1,2,3,4,5])
arr2 = array([6,1,9,3,2])

arr3 = [ ]
for f in range(0, len(arr1)):
    arr3.append(arr1[f] + arr2[f])
print(arr3)

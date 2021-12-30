
from numpy import *

arr1 = array([5,2,6,7,3,5])

arr2 = arr1.copy()

arr1[4] = 7

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))
'''
from array import *

num = array('i',[5,8,-4,8,2])

print(num)


from array import *

num = array('i',[5,8,-4,8,2])

print(num[3])


from array import *

num = array('I',[5,8,4,8,2])

for e in num:
    print(e)


from array import *

T_char = array('u',['a', 'b' , 'c', 'd'])

print(T_char)


from array import *

fun = array('u', ["s", "u", "n"])

for e in fun:
    print(e)


from array import *

num = array('i', [4,2,8,2,8,9,])

newArr = array(num.typecode, (a*a for a in num))

for e in newArr:
    print(e)


from array import *

vals = array('i',[2,3,4])

newArr = array(vals.typecode, (a*a for a in vals))

for e in newArr:
    print(e)
'''

from array import *

vals = array('i',[5,3,4])

newArr = array(vals.typecode, (a*a for a in vals))

i = 0

while i <len(newArr):
    print(newArr[i])
    i += 1







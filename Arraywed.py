
from array import *

vals = array('i',[2,5,6,8])

newArr = array(vals.typecode,(a*a for a in vals))

for e in newArr:
    print(e)
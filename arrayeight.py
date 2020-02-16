from array import*
vals = array('i',[5,9,8,4,2])
newArr = array(vals.typecode,(a for a in vals))
for e in newArr:
    print(e)

#[1,1,1,1,1
# 1,0,0,0,1
# 1,0,9,0,1
# 1,0,0,0,1
# 1,1,1,1,1]

import numpy as np
op=np.ones((5,5),dtype='int16')
z=np.zeros((3,3))
z[1,1]=9

#to replace val of op array (from row 1 to 3) and (column 1 to 3)
#op[1:4,1:4]=z 
op[1:-1,1:-1]=z 

print(op)

#Note: be carefull when copying matrix
a=np.array([1,2,3])
b=a.copy()
b[0]=100
print(b)
print(a)  # these both gives diff

b=a
b[0]=100
print(b)
print(a)# these both gives [100,2,3]


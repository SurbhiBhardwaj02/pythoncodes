import numpy as np

a=np.ones((2,3))
print(a)

b=np.full((3,2),2)
print(b)
 
#print(a*b) ValueError: operands could not be broadcast together with shapes (2,3) (3,2)
print(np.matmul(a,b)) # but here also check columns1=rows2

c=np.identity(3)
print(np.linalg.det(c)) #find the determinant
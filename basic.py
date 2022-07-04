import numpy as np
a=np.array([1,2,3],dtype='int16')  
print(a)
b= np.array([[7.0,6.0,5.0],[2,3.0,4.5]])
print(b)

#get dimensions
print(a.ndim)
print(b.ndim)

#get shape
print(a.shape)
print(b.shape)

#get type
print(a.dtype)
print(b.dtype)

#get size
print(a.itemsize)
print(b.itemsize)

#get total size
print(a.nbytes)
print(b.nbytes)
import numpy as np
 
old=np.array([[1,2,3,4],[5,6,7,8]])
print(old)

#new=old.reshape((2,3))   ValueError: cannot reshape array of size 8 into shape (2,3)
new=old.reshape((8,1))
print(new)

#vertically stacking matrix

v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])

print(np.vstack([v1,v2,v1,v1,v2]))

#horizontally  stacking matrix
h1=np.ones((2,3))
h2=np.zeros((2,2))
print(np.hstack((h1,h2)))

#you can index with a list in numpy

a=np.array([1,2,3,4,5,6,7,8,9])
print(a[[ 1,2,8]])
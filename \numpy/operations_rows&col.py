#Accessing /Changing specific elements,rows,columns etc

import numpy as np
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,145]])
print(a)

#get a specific elem. [r,c]

print(a[1,5])
print(a[0,4])

#get specific row
print(a[0,:])

#get specific column
print(a[:,2])

#get a lil more fancy [startindex:endindex:stepsize]
print(a[0,1:6:2])
#or
print(a[0,1:-1:2])

#edit
a[1,5]=20
#edit col
a[:,2]=[34,35]
print(a)

# 3d example
b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

#Get specific element (work outside in)
print(b[0,1,1])

#get printed second row of both inside arr
print(b[:,1,:])
#get printed first row of both inside arr
print(b[:,0,:])

    #edit
b[:,1,:] =[[9,9],[8,8]]
print(b)


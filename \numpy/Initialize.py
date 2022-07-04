#Initializing diff types of arrays
import numpy as np
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,145]])

print('All 0s matrix')
print(np.zeros((2,3,3,3)))
print("newwwww")
print(np.zeros((2,3,3)))
print('newww')
print(np.zeros((2,3)))

print('All 1s matrix')
print(np.ones((4,2,2),dtype='int16'))

print('Any other number')
#((shape),variable)
print(np.full((2,2),44,dtype='float32'))

print('Any other number (full_like)')
print(np.full_like(a.shape,4))
print(np.full_like(a,4 ))

print('Random decimal numbers')
print(np.random.rand(4,2))
print(np.random.rand(4,2,3))
print()
print(np.random.random_sample(a.shape))

print('Random int values')
print(np.random.randint(23,size=(3,3)))#gives random val till 0 to 23
print(np.random.randint(1,7,size=(3,3)))#gives random val btwn 1 &7

print('to make identity  square matrix cube etc')
print(np.identity(2))
print(np.identity(5))

print('repeat')
arr=np.array([[1,2,3]])
r1=np.repeat(arr,3)
print(r1)
r1=np.repeat(arr,3,axis=0)
print(r1)
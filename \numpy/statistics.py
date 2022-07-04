import numpy as np
stat=np.array([[1,2,3],[4,5,6]])
print(stat)

print(np.min(stat))

print(np.min(stat,axis=0))#rows axis=0
print(np.min(stat,axis=1))#column axis=1

print(np.max(stat))
print(np.max(stat,axis=1 ))
print(np.max(stat,axis=0  ))

print(np.sum(stat))
print(np.sum(stat,axis=1))
print(np.sum(stat,axis=0))
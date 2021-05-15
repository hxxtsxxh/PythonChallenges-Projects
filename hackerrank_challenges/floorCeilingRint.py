import numpy as np
np.set_printoptions(legacy = '1.13')

A = input().split()
a = np.array(A, float)

print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))

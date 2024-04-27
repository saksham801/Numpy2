# ARRAY ATTRIBUTES 

import numpy as np

a1 = np.arange(10)
print(a1)

a2 = np.arange(12 , dtype=float).reshape(3,4)
print(a2)

a3 = np.arange(8).reshape(2,2,2)
print(a3)

# ndim :- to find the dimension of array 

print("dimension of a1 :- ", a1.ndim)
print("dimension of a1 :-",a2.ndim)
print("dimension of a1 :-",a3.ndim)


# shape :- number rows and columns

print(a1.shape)
print(a2.shape)
print(a3.shape)

# size :- count the number of items in array

print(a1.size)
print(a2.size)
print(a3.size)


# itemsize :- how much space occupy in memory
print("Itemsize")
print(a1.itemsize)
print(a2.itemsize)
print(a3.itemsize)

# dtype :- check what is data type 

print("dtype")
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)
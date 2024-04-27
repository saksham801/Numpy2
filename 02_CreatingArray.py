import numpy as np

a = np.array([1,2,3])

# Printing array 
print(a)

# find the type of array 
print(type(a))


# creating 2d Array
print("2D Array")
b = np.array([[1,2,3,4],[5,6,7,8]])
print(b)

# Creating 3D array 
print("3D Array")
c = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,2,3]]])
print(c)


# dtype :- Data type use like float , bool , complex

d = np.array([1,2,3,4] , dtype=float)
print(d)

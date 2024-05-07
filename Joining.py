# Joining the numpy array - Here for this we will pass concatenate().
import numpy as np
array1 = np.array([1, 2, 3, 4, 5 ])
array2 = np.array([6, 7, 8, 9, 10])
print(np.concatenate((array1, array2)))
# print(array1 + array2)
# Joining the 2-d array with rows (axis = 1)
d2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
d3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
n = np.concatenate((d2, d3), axis = 1)
print(n)

# Joining array using the staok function
saksham = np.array([1, 2, 3, 4, 5])
saksham1 = np.array([6, 7, 8, 9, 10])
saksham2 = np.concatenate((saksham, saksham1), axis = 0)
saksham3 = np.stack((saksham, saksham1), axis = 0)
print(saksham2)
print(saksham3)

# hstack
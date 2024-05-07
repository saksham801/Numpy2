# If we have to add or join the array we use np.concate() function
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.concatenate((arr1, arr2))
print(arr3)
print()

# Joining the 2-d array using rows and column
arr4 = np.array([[1, 2], [3, 4]])
arr5 = np.array([[5, 6], [7, 8]])
arr6 = np.concatenate((arr4, arr5), axis=1)  # Axis 1 can print in horizontal and axis 0 can print in vertical format
print(arr6)
print()

# Joining 1-d array using stack() function in numpy
# Stack () function allow us to concatenate with a new axis
# It convert 1-d into 2-d and 2-d into 3-d
arr7 = np.array([[1,2,3],[7,8,9]])
arr8 = np.array([[4,5,6],[10,11,12]])
arr9 = np.stack((arr7, arr8),axis=1)
print(arr9)
print()

# Stacking along with rows using hstack() function
# hstack allows us to join the array without converting their respective dimension
arr10 = np.hstack((arr7,arr8))
print(arr10)
print()

# Stacking along with column using vstack()
# vstack allows us to print with column
arr11 = np.vstack((arr1,arr2))
print(arr11)
print()

# Stacking along with height(depth)
# Using dstack
arr12 = np.dstack((arr1,arr2))
print(arr12)
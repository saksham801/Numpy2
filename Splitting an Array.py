# In split allows us to break a array in one or more part according to choice .
# We use array_split() function to perform the spliting
import numpy as np
array1 = np.array([1, 2, 3, 4, 5, 6])
array2 = np.array_split(array1, 3)
print(array2)
print()


arr3 = np.array([1, 2, 3, 4, 5, 6])
arr4 = np.array_split(arr3, 4)
print(arr4)
print()


# Accessing an array with index
print(array2[0])
print(array2[1])
print(array2[2])
print()

# Spliting the 2-d array
arra2d = np.array([[1, 2],[3, 4],[5, 6]])
arr5 = np.array_split(arra2d, 3)
print(arr5)

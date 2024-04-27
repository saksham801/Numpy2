# Copy = We can only change the variable which it can be created from other
# We will make a copy, change in original array, and display both.
import numpy as np
array1= np.array([1,2,3,4,5])
array2 = array1.copy()
print(array2)
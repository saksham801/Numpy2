# Use to Change the data type in lower datatype i.e means to ocuppy less amount of memory consumption 

import numpy as np 

a1 = np.array([1,2,3] , dtype="int64")
print(a1)
print(a1.dtype)
print(a1.itemsize)

# change the data type :- astype
a1 = a1.astype("int32")
print(a1.dtype)



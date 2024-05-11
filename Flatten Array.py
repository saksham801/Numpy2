# Flatten function help us to get the multidimensional array into 1d array
from numpy import *
a = array([[[1, 2, 3],[4, 5, 6],[7, 8, 9]]])
print(a)
print(a.flatten())
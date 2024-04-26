# Means going through element one by one or step by step
# Like for loop
# If we have get the element in the form of single element we have to use nested for loop.
import numpy as np
a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
for i in a:
    for j in i:
        print(j)

# 2-d
b = np.array([[1,2,3],[4, 5, 6]])
for i in b:
    print(i)
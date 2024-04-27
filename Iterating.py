# Means going through element one by one or step by step
# Like for loop
# If we have get the element in the form of single element we have to use nested for loop.
import numpy as np
a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(a.ndim)
for i in a:
    for j in i:
        print(j)

# 2-d
b = np.array([[1,2,3],[4, 5, 6]])
for i in b:
    print(i)

# Iterate on each scalar element of the 2-d
b = np.array([[1,2,3],[4, 5, 6]])
for i in b:
    for j in i:
        print(j)

print("3-d")
c = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
for i in c:
    for j in i:
        for k in j:
            print(k)


print('nditer')
# Iterating arrays using the nditer() function.
# Now we will iterate on rach scalar element.
# Instead of using nested loop we can use nditer.

array = np.array([[[1,2],[3,4],[5,6]]])
for i in np.nditer(array):
    print(i)

# Now we will skip the element in iteration.
print("Skiping the element")
for i in np.nditer(array[:,::2]):
    print(i)

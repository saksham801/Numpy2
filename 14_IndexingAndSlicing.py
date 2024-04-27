import numpy as np

a1 = np.arange(10).reshape(2,5)
print(a1)

# indexing 
# postive indexing --> from 0 
# negative indexing --> from -1 

array = np.array((1,2,3,4))
print(array)
#accessing element 
elem = array[0]
elem1 = array[1]
elem2= array[2]
elem3 = array[3]
print(elem , elem1 , elem2 , elem3)


# 2d array accessing element

a1 = np.arange(10).reshape(2,5)
print(a1)

element = a1[1,2]
print(element)


# accessing in 3d
a3 = np.arange(12).reshape(3,2,2)
print(a3)

print(a3[1,1,1])


print(a3[0,0,0])



# Slicing 

# 1D array
a1 = np.arange(10)
print(a1)

print(a1[2:5])

# 2d Array 

a2 = np.arange(20).reshape(4,5)
print(a2)

# for rows slicing
print(a2[0,:])
print(a2[1,:])
print(a2[2,:])
print(a2[3,:])

# for columns slicin

print(a2[:,0])
print(a2[:,1])
print(a2[:,2])
print(a2[:,3])

# for specific value from matri

print(a2[1:3,2:4])


# 3d matrix 

a3 = np.arange(27).reshape(3,3,3)

print(a3)


print(a3[1])
print(a3[::2])
print(a3[0,1,:])

print(a3[1,:,1])
print(a3[2,1:,1:])
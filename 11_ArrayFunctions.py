import numpy as np

a1 = np.random.random((3,3))
a1 = np.round(a1*100)
print(a1)

# max 

max_a1 = np.max(a1)
print(max_a1) # check the overall matrix and find out the max value 

# to find the rows and columns wise max value 
# col --> 0 and rows --> 1

rows_max_a1 = np.max(a1 , axis=1)
print("rows wise max value:- ",rows_max_a1)

col_max_a1 = np.max(a1 , axis=0)
print("columns wise max value :- ",col_max_a1)



# min 
print(a1)
min_a1 = np.min(a1)
print(min_a1)

# column wise min value 
col_min_a1 = np.min(a1 , axis=0)
print(col_min_a1)

# row wise min value 
row_wise_min = np.min(a1 , axis=1)
print(row_wise_min)

# sums 
print(a1)
sums = np.sum(a1)
print(sums)

# col sum s

col_sum = np.sum(a1 , axis=0)
print(col_sum)

# row sums 

row_sums = np.sum(a1 , axis= 1)
print(row_sums)


# prod 

product = np.prod(a1)
print(product)

# col wise product 
col_prod = np.prod(a1,axis=0)   
print(col_prod)

# row wise product

row_prod = np.prod(a1,axis=1)
print(row_prod)


# mean 
# also find the col and rows wise mean 

mean = np.mean(a1)
median = np.median(a1)
stand = np.std(a1)
variance = np.var(a1)
print("Mean value :- ",mean)
print("Meadian value :- ", median)
print("standard Deviation :- ", stand)
print("Variance :- ", variance)


# trigo 
# same for all other 
sin = np.sin(a1)
print(sin)


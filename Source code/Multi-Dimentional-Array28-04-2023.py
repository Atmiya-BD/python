# multi dimensional arrays

# the 2d arrays, 3d arrays etc. are hold multidi-mensional arrays

from numpy import *

# a=array([[10,11,12,13],[14,15,16,17]])
# print(a)

# the internal memory allocted to all the elements would be in a single row containing 8 digit blocks(at there 8 elements in the array)

# the elements are stored in the contiguous memory location as shown below
# (screenshot)

# the reshape() function

# this function is used to convert a 1d array into a multi-dimensional array
# it would written as below

# reshape(arrayname, (n,r,c)) here n is optional argument

# here 'n' represents the number of array in the output, 'r' represents row and 'c' represents number of columns

# a=array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(a)
# b=reshape(a, (4,3))
# b=reshape(a, (3,4))
# b=reshape(a, (3,3,2))
# print(b)

# indexing in multi-dimensional array

# index represents the location number.
# the individual elements of 2d array can be accessed by specifying the location no of the row and columns of the element in the array as

# a[0][0] #it represents the 0th row and 0th column
# a[1][3] #it represents the 1st row and 3rd column

# a=array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(a)

# for i in range(0,len(a)): #for rows
#     # print(a[i])
#     # for j in range(0,len(a[i])): #for columns
#         # print(a[i][j], end=" ")
#         # print(a[i],[j])

# slicing in multi-dimensional arrays
a=array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
# print(a[0,:]) #(n,c)
# print(a[2,:]) 
# print(a[:,0]) 
# print(a[0:1,:])
# print(a[2:3,1:2])
# print(a[2,:1])
# print(a[2,:2])
# print(a[0,1])
# print(a[0,0:4])
# print(a[0,1:3])

# print(a[0:1])
# print(a[0,2: 1])
# print(a[2: ])

print(a[0,0])
print(a[0,1])
print(a[0,2])
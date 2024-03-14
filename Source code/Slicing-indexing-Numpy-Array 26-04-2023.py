# slicing and indexing numpy arrays

# slicing refers to extracting a ragne elements of array
# the format of slicing operation is as below

# arrayname[start: stop: stepsize]

# here the default value of 'start' is 0, for 'stop' is n(number of elements), stepsize is 1

# counting starts from 0th position

from numpy import * 
# a=array([1,2,3,4,5,6,7,8,9,10,11])
# print(a)

# retrieving 1st element to 6th elements
# print(a[1:5])

# retrieving 1st element to 6th elements alternatively
# print(a[1:5:2])

# retrieving all the elements
# print(a[:])
# print(a[::])

# retrieving all the elements from 3rd element
# print(a[3:])

# retrieving all the elements from 3rd element alternatively
# print(a[3::2])

# indexing
# indexing refers to location of the elements. by specifying the location of the number from 0 and onwards till n-1, we can refers all elements as a[i] where 'i' can change from 0 to n-1

# i=0
# while(i<len(a)):
#     print(a[i], end=" ")
#     i=i+1

# attributes of array 
# ndim attribute 
# shape attribute 
# size attribute
# dtype attribute 

# reshape() method
# flatten() method

# the ndim attribute
# the ndim attribute represents the number of dimensions of the array.

# for a single dimensional array it will display 1 and for tow dimensional array it will display 2 

# n-number
# dim-dimensions
# a=array([1,2,3,4,5,6,7,8,9,10,11])
# print(a)
# print(a.ndim)

# b=array([[1,2,3,4],[1,2,3,4]])
# print(b)
# print(b.ndim)

# c=array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
# print(c)
# print(c.ndim)

# d=array([[[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]]])
# print(d)
# print(d.ndim)

# the shape attribute
# the shape attribute gives shape of array

# the shape of a tuple listing the numbers of elements along each dimensions
# a=array([1,2,3,4,5,6,7,8,9,10,11])
# print(a)
# print(a.shape) #(cols)

# b=array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
# # b=array([[1,2,3,4],[1,2,3,4],[1,2,3]])#this is not valid
# print(b)
# print(b.shape) #(row, cols)

# b.shape=(4,3) #(row, cols)
# b.shape=(4,2) #(row, cols) #this is not valid
# b.shape=(6,2) #(row, cols)
# print(b)
# print(b.shape) #(row, cols)

#the size attribute
# the size attribute gives the total number of elements in the array
# a=array([1,2,3,4,5,6,7,8,9,10,11])
# print(a.size) 

# b=array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
# print(b)
# print(b.size)

# d=array([[[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]]])
# print(d)
# print(d.size)

# the dtype attribute
# the dtype attribute gives the datatype of the array elements

# a=array([[1,2,3,4],[1,2,3,4]])
# print(a.dtype)

# a=array([[1,2,3,4],[1,2,3,4.4]])
# print(a.dtype)

# a=array([[1,2,3,4],[1,2,3,'a']])
# print(a.dtype)

# the reshape() method
# the reshape() method is used to change the shape of an array

# a=array([1,2,3,4,5,6,7,8,9,10])
# # a=array([1,2,3,4,5,6,7,8,9]) #this is not valid
# a=a.reshape(2,5) #(row, cols)
# print(a) 

# the flatten() method
#  the flatten() method is usefult to collapse the elements of an array into one dimensional array
# a=array([[1,2,3,4],[1,2,3,'abc']])
# a=a.flatten() 
# print(a) 
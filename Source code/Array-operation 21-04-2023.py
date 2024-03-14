# operations on array

# from numpy import *

# ar=array([40,20,30,60,90])

# print(ar)

# print("adding 5 to each element of array: ", ar+5)
# print("subtractinging 5 to each element of array: ", ar-5)

# print("MULTIPLYING 5 to each element of array: ", ar*5)
# print("DIVIDING 5 to each element of array: ", ar/5)

# print("the biggest element of array: ", max(ar))
# print("the smallest element of array: ", min(ar))

# print("the addition of all elements of array: ", sum(ar))
# print("the average of all elements of array: ", mean(ar))

# comparing arrays

# from numpy import *
# a=array([40,20,30,60,90])
# b=array ([40,40,30,90,60])

# print(a==b)
# print(a!=b)

# print(a>b)
# print(a<b)

# print(a>=b)
# print(a<=b)

# compare corresponding elements of two arrays and retrieve the biggest elements

# from numpy import *
# a=array([40,20,30,60,90])
# b=array ([40,40,30,90,60])
# # c=a>b, a,b
# c=where(a>b, a,b) #use of where() function
# c=where(a<b, a,b)
# c=where(a<b, b,a)
# print(a)
# print(b)
# print(c)

# the where functin can be use to create new array based on whether a given condition is true or false
# the syntax of the where functin 
#       syntax: array=where(condition, expression1, expression2)
# the use of where() function  is demonstrated in the above example

# a program to retrive non zero element from the array
# from numpy import *

# a=array([4, 0,20,30,6, 0,9, 0, ])
# b=nonzero(a) #use of nonzero()
# print(a)
# print(a[b])

# the nonzero() function
# the nonzero() function is used to retrieve the non zero elements from the array

# program to create a view of an existing array
# from numpy import *

# a=array([4, 0,20,30,6, 0,9, 0, ])
# b=a.view() # here 'b' array is mirror of array 'a'

# print(a)
# print(b)

# print(id(b))
# print(id(a))

# b[2]=320
# print(a)
# print(b)

# a[3]=-320
# print(a)
# print(b)

# view- mirror effect / mirror creator

# a view() function create same array as existing array
# the original array and the new created array will share different memory locations

# if the newly created array is modified, the original array will also be modified and vice-versa
# view() function creates a copy which is known as 'shallow copying'(chicharu) Vs 'deep copy'
# the use of view() function is demonstrated in the above program

# in case we want both array but modifing one array must not have and effect on another array the we may use the copy function.
# the use of copy() function is demonstrated in the below program

# for deep copy in copy() function is use
# from numpy import *

# a=array([4, 0,20,30,6, 0,9, 0, ])
# b=a.copy() # here 'b' array is mirror of array 'a'

# print(a)
# print(b)

# print(id(b))
# print(id(a))

# b[2]=320
# print(a)
# print(b)

# a[3]=-320
# print(a)
# print(b)
# indexing & slicing

# indexing
# an index represents the position number of elements in the array. for example when we create a array like this(a=array('i', [10,20,30,40,50,60])). python interpreter allocates 5 blocks of memory
# here 0,1,2 extra are representing the position numbers of the elements. so in general we can use "i" to preresent the position of any element.
# this "i" is called index of the array

# copying the elements of an array to another array

from array import *
# c=array('u', ['a', 't', 'm', 'i', 'y', 'a'])
# d=array(c.typecode, (a for a in c))
# for ch in d:
#     print(ch)

# indexing and slicing on arrays using array index and for loop
# a=array('i', [10,20,30,40,50,60])
# n=len(a) #finds numbers of elements in an array
# print('length of the array: ',n)

# for i in a:
#     print(i, end=" ")
# for i in range(n):
#     print(a[i], end=" ")

# indexing and slicing on arrays using array index and while loop
# i=0
# while (i<n):
#     print(a[i], end=" ")
#     print(i)
#     i=i+1

# Slicing 

# a slice represent a peace of the array. slicing is useful to retrive arrange of elements. the general format of a slice is 
# format:
    # array_name(start : stop : stride/jump)

# we can eleminite any one or any two from the above three

# c= array('u', ['a','t','m','i','y','a','u','n','i','v','e','r','s','i','t','y'])
# a=c[0:15]
# a=c[0:16]
# a=c[1:16]
# a=c[:16]
# a=c[0:]
# a=c[:4] #0to3 (last index is excluted)
# a=c[3:8]
# a=c[-16:]
# a=c[-16:-5]
# a=c[-16:5]
# a=c[1:15:2]
# print(a)

# for i in c[0:12]:
#     print(i, end=" ")

# for i in c[0:12:2]:
#     print(i, end=" ")

# indexing vs sliceing
# indexing -> whole array
# sliceing -> selective/user wanted elements
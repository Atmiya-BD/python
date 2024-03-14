# pass statement in python
# -> pass statement is used as 'placeholder' for future code.
# -> when the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
# -> empty code is not allowed in loops, fucntion definitions, class definitions or in if statements(some times).
# -> usin pass inside loop, function or a class gives you a ficility to keep it empty
# pass statement is used when we need a statement syntectically but we do not do any operation
# -> the difference between pass and comment is that comment is ignored by the interpreter where is pass is not ignored.

# a=0
# while a<10:
#     a=a+1
#     if a>5:
#         pass
#     print(a)

# stub(dummy code)

# program to display only negative values from the list
# a=[1,2,3,6,-96,-3,2,-7,14,-36]
# for i in a:
#     if i>0:
#         pass
#     else:
#         print(i)

# array in python
# -> an array is an object that stores a group of elements with same data type.
# -> the main advantage of an array is to store and process a group of elements easily
# -> an array can store only one type of data. it means we can store only integer type or only float type elements in to an array at a times.
# -> but we can not store one integer value, one float and one character type element into the same array.
# -> an array can increase of decrease there size size dynamically. it means we need not declare the size of an array. where element are added it will increase it size and when element are removed it wwill automatically decrease it size in memory.

# advantage of an array
# -> arrays are similar to list. the main difference is that array can store only one type of elements list can store different type of elements
# -> when dealing with huge numbers of elements array uses less memory then list
# -> arrays offer faster execution then list

# import array 
# syntax:
# arrayname = array(type code, [elements])

# creating an array
# Table form the screenshot

# to deal with array we need to import array module

# three ways to imoport array module into our program
# when we import array module we are able to get the array class of that module that helps us to create an array

# way-1
# import array
# a=array.array('i', [10,206,-90.33])
# a=array.array('i', [10,206,-90])
# print(a)

# here the first 'array' represents a module name and the next 'array' represents the class name for which object is created.

# way-2
# import array as ar
# b=a.array('f', [10,206,-90.36,])
# print(b)

# here 'ar' is an alias of array module

# way-3
# from array import *
# c=array('i', [1,2,5,5,55,95,-96])
# print(c)

# -> using chracters in the array by using type code 'u'

# from array import *
# c=array('u', ['a','d','e','t'])
# # c=array('u', ["a", "b","c"])
# print(c)

# the meaning of this statement is import all(classes, objects, function, etc) from the array module into our program so there is no need to mention array module name while creating 

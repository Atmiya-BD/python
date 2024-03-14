# returning multiple values from a function

# a function in python can ruturn multiple values
# when function calculate multiple results and wants to return all those results we can use return statement as "return a,b,c"
# this values are writted by a function in the form of tuple
# performing basic arithmatic operations using functions 
# def arith(a,b):
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return add, sub, mul, div

# p,q,r,s=arith(10,50)

# print("the result is: ", p,q,r,s)

# pass by object reference / pass by object

# immutable objects in python: int, float, string, tuple,  
# mutable objects in python: list
 
# using: immutable mutable object int
# def modify(a):
#     a=16
#     print('the value of a inside the function is: ', a,id(a))

# #call the function
# a=10
# modify(a)
# print('the value of a outside the function is: ', a, id(a))

# using: mutable object list
# def modify(lst):
#     lst.append(15)
#     print(lst, id(lst))

# # calling the function
# lst=[10,20,30,40,50,60]
# modify(lst)
# print(lst, id(lst))

# as the value assigned to variable 'a' is of integer type, modifying the value of 'a' will be not be stored at same memory address as integer is immutable, modifying value of a will occupy another memory to store a new value of new 'a'.

# formal and actual arguments 
# def sum(a,b): --> fromal arguments
# a=10,b=20
# sum(a,b) --> actual arguments

# the actual arguments are of 4 types:
    # - positional arguments
    # - keyword arguments
    # - default arguemnts
    # - variable length arguments

# positional arguments
# what is position arguments?

from ast import arguments


# the number of arguments and their position in the function definition should match exatly match and positon of the arguments in the function call

def combi(s1,s2):
    s3=s1+s2
    print(s3)

# calling the function
combi("good", "morning") #i/O: good morning
combi( "morning", "good" ) #i/O: morning good
combi( "morning", "good", "student" ) # take 2 positional arguments but 3 were given
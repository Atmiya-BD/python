# keyword arguments 
# keyword arguments are arguments that identify the paramenters by their names

# at the time of calling function, we have to pass two values and we can mansion which value is for what
# def  student (rno, name):
#     print("roll is: ", rno)
#     print("name is: ", name)

# student(name='abc', rno=55)
# student( rno=15, name='dk')

# default arguments
# if required we can set a default value to the parameter if at the time of calling function the value is not passed to the argument then default value will be used. and if the value is passed to the argument then the passed value wil be used 

# def stud(no, name='user'):
#     print("roll no is: ", no)
#     print('name is: ', name)

# stud(10)
# stud(10, 'jk')

# variable length arguments
# in some situation it is possible that the programmer is unware about the requirements of the paramenters in the program if in program two parameters are declared, and while using it user feel to give more then two values then error will occur.

# in that case variable length argument can be used.
# a variable length argument is an argument that can accept any number of values 

# formet: def name_of_function (farg, *args)
# def add(farg, *args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     print("sum of all numbers: ", (farg+sum))

# add(10,20)
# add(10,20,20)
# add(10,20,30,44.44)

# passing a group of elements to a function
# some time it is required to receive group of elements like numbers or strings, we can accept them in to a list and then pass the list to the function

# example:
# def show(lst):
#     for i in lst:
#         print(i)

# # taking group of strings as an input
# print("enter strings seperated by space: ")
# lst=[a for a in input().split(' ')]

# show(lst)

# anonymous function(which is also known as lambda)
# we already know that while writing a function we need to give name to the function 
# we usually do it like 
#   def name_of_function(argument) 
# but the anonymous function it is definded with the keyword lambda

# def square(a):
#     return a*a

# this could be written in anonymous function as:
# lambda a:a*a

# find the square of the entered number
# a=int(input(' enter the number: '))
# ans=lambda a:a*a
# print("the square of the entered number is: ", ans(a))

# big=lambda a,b:a if a>b else b

# a,b=[int(n) for n in input('enter two numbers comma seperated: ').split(',')]
# print(f'the bigger number out of two number is : ', big(a,b))

# generators
# generators are function that return a sequence of values. a generator function is written like ordionary functions but it uses 'yield' statement.
# the 'yield' statement is usful to return the value.

# what is meant by yield statemnt? it is used in generators
# program to create generator that returns a sequence of number from x to y
def gen1(x,y):
    while x<=y:
        yield x
        x=x+1 

# fill generator object with 1 and 10
gen=gen1(1,10)
# display the values
for i in gen:
    print(i, end="")
print(next(gen))

# function vs generator
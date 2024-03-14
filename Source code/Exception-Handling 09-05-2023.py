# errors in a python

# Exception 

# an exception is an event which occurs during the execution of the program that changes is the normal flow of the program's instructions 

# an exception is runtime error which can be handled by the programmer 

# it means if the programmer can gus an error in the program end he can do something to eleminate the harm caused by the error, then it is called an exception.

# if the programmer can not do anything in case of error, then it is called an error not an exception

# all exceptions are represented in classes in python. the exception which are already available in python are called built-in exception

# the base class of all built-in exception is 'BaseException' class

# Exception Handling

# exception handling is process of responding to unwanted or unexpected events when a computer programs runs

# exception handling deals with this events to avoid to avoid the program or system crashing

# the purpos of exception handling is to give a proper error message to the user when an error occurs

# to handle exception program should perform following three steps:
    # step:1 - the programmer shoudl observe the statement in his program where there may be possibility of exception. such statements must be written in side the 'try' block
    # syntax:
    # try: 
    #     statements

    # if an error aries inside the 'try' block the program will not be terminated. 
    # the PVM will understand that there is an exception, it will jump into an 'except' block

    # step:2 - the programmer shoudl write the except block where he should display the exception details to the user.
    # the programmer should also display an error message regarding what can be done to avoid this error

    # syntax:
    # except exceptionName:
    #     statements

    # statements written inside an 'except' block are called 'handlers' since they handle the situation 

    # step:3 - the programmer should perform clean up actions like closing the file and terminating any other process which are running. it should be written 'finally' block

    # syntax:
    # finally:
        # statements

    # the speciality of 'finally' block is that the statements inside the finally block are executed irrespective of whether there is an error or not 

    # performing the above the task is called excption handling 

    # Note: - a single 'try' block can be followed by multiple 'except' blocks 
        # - 'except' blocks can not be written with try block
        # - writing 'except' block and finally block is not mandatory 
        # - 'finally' block if written then will always executed

# error vs exception

# a=10

# if a==10:
#     print('the value of a is 10')

# def contact(a,b):
#     try:
#         print(a+b)
#     except:
#         print('cannot concat string with integer')

# contact("i like mango", 100)

# fruits=['mango', 'banana', 'apple']
# try:
#     print(fruits[3])
# except:
#     print('element does not exist')

# example
# try:
#     a=int(input("enter a value: "))
#     b=int(input("enter a value: "))
#     print(a/b)
# except:
#     print('number cannot be divided with 0')


# def increment(sal):
#     sal=sal+sal*15/100
#     return sal

# print(increment(4000))

# try:
#     print('you are in the try block')
#     a=int(input("enter a value: "))
#     b=int(input("enter a value: "))
#     c=a/b
# except:
#     print('number cannot be divided with 0')
# else:
#     print('you are in else part')
#     print('the answer of division is: ', c)
# finally:
#     print('you are in finally block')
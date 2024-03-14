# looping and control structure, arrays, strings

# if statement

# the if statement is used to execute one or more statements depending upon the wheter condition is true or not

# syntax:
#     if condition:
#         statements

# first the condition is tested. if the condition is true then the statements given after colon are executed

# we cṇan write one or more statements after colon. if the condition is false then the statements given after colon are executed mensioned after colon are not executed


# if a==1:
#     print ('the value of a is: 'a)

# a=int(input('enter the value of a: '))
# if a>7:
#     print('the entered value is greater then 7')
#     print('thank you')

# a=int(input('enter the value of a: '))
# if a>0:
#     print('the value you entered is positive')

# a='atmiya'
# if a=='atmiya':
#     print('the value of a is Atmiya')

# a=int(input('enter the value of a: '))
# b=int(input('enter the value of b: '))

# if a>b:
#     print('the value of a is greater than b')

# a=int(input('enter the value of a: '))
# b=int(input('enter the value of b: '))

# if a==1:
#     print('the value of a is greater than b')
#     if b==2:
#         print('the value of b is 2')
# print('end of program')

# quantity=int(input('enter the quantity: '))
# price=5
# if price*quantity<10000:
#     print('the bill amount is less than Rs. 10000, we cannot dispatch your order')
#     print('pleace increase your quantity')

# if...else statement
# the if else statement executes a group of statements when a condition is true otherwise it will execute another group of statements

# syntax:
#     if condition:
#         statement 1
#     else:
#         statement 2

# a=int(input('enter the value of a: '))
# if a%2==0:
#     print('the enter number is an even number')
# else:
#     print('the enter number is an odd number')

# a=int(input('enter the value of a: '))
# if a==1:
#     print('the value of a is 1')
# else:
#     print('the value of a is other than 1')

# a=input('enter the value of a: ')
# if a=='atmiya':
#     print('user has entered atmiya as input')
# else:
#     print('user has entered',a)

a=input('enter the value of a: ')
if a=='atmiya':
    print('user has entered atmiya as input')
    print('the value got matched')
else:
    print('user has entered',a)
    print('the value does not got matched')

a=int(input('enter the value of a: '))
b=int(input('enter the value of b: '))

if a>b:
    print('the value of a is smaller than value of a')
else:
    print('the value of a is smaller than value of b')
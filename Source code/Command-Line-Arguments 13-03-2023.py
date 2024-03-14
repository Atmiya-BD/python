# command line arguments

# we can write a program which can accept the values while we are running our program in the command prompt
# command line arguments are the arguments which are passed to the program from the outside the program
# artuments must be entered by keeping white space between them
# the arguments passed at the command line are by default stored in the form of list
# with the name 'argv' which is the part of 'sys' module

import sys

# print(sys.argv)
# a=sys.argv
# print(a)

# print(('the file name is :',a[0]))

# print(type(a))
# print(id(a))

# write a program to accept the two value from the user at the command line and add them
# a=int(sys.argv[0])

# a=int(sys.argv[1])
# b=int(sys.argv[2])

# sum=a+b
# print('the sum of a & b is: ', sum)

# print("Address of sys var: ",id(sys.argv))
# print("Type of sys var: ",type(sys.argv))

# command line arguments with 'argparse'
# the 'argparse' module in python is useful to develop user friendly programs using command line arguments 
# the 'argparse' module generates help and usage messages when user gives the program invalud arguments
# it may also display an error messages to the users
# to work with 'argparse', we must import it as 'import argparse'
# if 'argparse' is not installed then install it using command 'pip install argparse' in the command prompt

# to work with argparse module it is necessary to import it as 
# 'import argparse'
# the we should create an object of 'ArgumentParser' class object with description of the progra

import argparse
parser=argparse.ArgumentParser(description='enter any integer value, program will give you the square of it.')

# the next step is adding arguments to the parer using add_argument() method.

# a program may have one or more arguments that are to be inputed by the user at the time of running the program

parser.add_argument("no", type=int, help='please insert one integer number')

# in the above statement "no" represents the variable where arguments is stored
# type=int means user can enter only integer value
# help represents help message displayed to the user
# the parser will parse(go through) the arguments provided by the user
# this arguments are received by pars_args() method as 
args=parser.parse_args()

# write a program to find the square of a given number using argparse in command line

import argparse
parser=argparse.ArgumentParser(description='enter any integer value, program will give you the square of it.')

parser.add_argument("no", type=int, help='please insert one integer number')#here no is variable

args=parser.parse_args()
ans=args.no**2
print('the square of the inserted number is : ',ans)

# parser.add_argument("no1", type=int, help='please insert one integer number')
# parser.add_argument("no2", type=int, help='please insert one integer number')




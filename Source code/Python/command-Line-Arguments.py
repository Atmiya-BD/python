#Command line arguments
# import sys
# print(sys.argv)
#Write a program to display the name of Python file
# import sys
# a=sys.argv
# print ('The file name is: ',a[0])
#Write a program to accept two values from the users at command line and add them.
import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
sum=a+b
print('The sum of a and b is: ', sum)

#Command line arguments with 'argparse'
#Write a program to find the square of a given number using argpase in command line
# import argparse
# parser=argparse.ArgumentParser(description="Enter any integer, a program will give you a square of the number")
# parser.add_argument("no",type=int,help="Please insert one integer number")
# args=parser.parse_args()
# ans=args.no**2
# print('The square of the inserted number is: ', ans)

# #Program to add two numbers using command line arguments and argparse
# import argparse
# parser=argparse.ArgumentParser(description='enter two integer numbers, program will give you sum of it')
# parser.add_argument('n1',type=int,help="Please insert one integer value")
# parser.add_argument('n2',type=int,help="Please insert one integer value")
# args=parser.parse_args()
# sum=args.n1+args.n2
# print('The sum of two number is: ', sum)

#Program to accept multiple values from the user
# import argparse
# parser=argparse.ArgumentParser(description='Enter values as required')
# parser.add_argument('val',nargs=1)
# args=parser.parse_args()
# for a in args.val:
# 	print(a)
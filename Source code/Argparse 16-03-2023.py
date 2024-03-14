# program to add two number using command line arguments and argparse

import argparse

parse=argparse.ArgumentParser(description="enter two integers numbers, program will give you same of it")

parse.add_argument('n1', type=int, help="pleac insert ")

# program to assept multiple values from the user 

parse=argparse.ArgumentParser(description="enter values as required : ")

parse.add_argument('val', nargs='*')
args=parse.parse_args()

for a in args.val: 
    print(a)

# nargs='+'  -> here minimum 1 value required
# nargs='*'  -> here 0 value is possible
# nargs='1'

# 'nargs' keyword
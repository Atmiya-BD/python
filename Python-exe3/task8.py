# 8). Make an arrangement in such a way that user can enter only two values at the command line and perform
#  all the arithmetic calculations.

import argparse

# parse=argparse.ArgumentParser(description="enter two values separated by spcace: ")

# parse.add_argument('val', nargs='2')
# args=parse.parse_args()

parser=argparse.ArgumentParser(description='enter any integer value, program will give you the square of it.')
parser.add_argument("no", type=int, help='please insert one integer number')#here no is variable

args=parser.parse_args()
ans=args.no**2
print('the square of the inserted number is : ',ans)



# 6). Following the instruction of Q5, display the output as below:
#  The name of file is abc.py and its values are [values added at command line].

import sys

# print('name of file is: ', sys.argv[0])
# print('Values are added at comm: ', sys.argv[1:])

print('The name of file is: ',sys.argv[0] ,'\nand its values are: ',sys.argv[1:])

# 7). Take one numeric value from the user using argparse and display value after adding 2 to it

import sys

print(sys.argv)

val=int(sys.argv[1]);

print("your entered value is: ",val)
print("after adding 2 in value it become: ",val+2)
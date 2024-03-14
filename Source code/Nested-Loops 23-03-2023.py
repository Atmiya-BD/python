# nested loops

# nested loops mean loop inside loop
# in python programming language there are two types of loops 1. while loop 2.for loop
# using this loop we can create  nested loops
# for example while loop inside the for loop, for loop inside the for loop etc.
# the inner loop will be executed 1 time for each iteration of the outer loop

# structure:
#     outer loop:
#         inner loop:
#             inner loop:

# for i in range(2):
#     for j in range(3):
#         print("i=",i,"j=",j)

# for i in range(0,2):
#     for j in range(0,3):
#         print("i=",i,end=" ")

# for i in range(2):
#     for i in range(3):
#         for i in range(4):
#             print("i=",i)

# for i in range(3):
#     for j in range(4):
#         print(i, end=" ")
#     print()

# NOTE:  outer loop is incharge of rows and inner loops is incharge of columns

# create seqare/rectangle by acceting rows and columns and symbole from user
rows=(int(input("enter number of rows:")))
columns=(int(input("enter number of columns:")))
symbol=(input("enter number of symbols:"))

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end=" ")
#     print()

# left aligned, right aligned triangle
for i in range(0,rows):
    for j in range(0,i):
        print(symbol, end=" ")
    print()


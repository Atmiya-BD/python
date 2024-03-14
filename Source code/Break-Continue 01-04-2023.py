# 01-04-2023
# break and continue

# the break statement
# the break statement in python works as a loop control statement
# it can be used in side a for loop, while loop or nested loop to come out of the loop
# when break statement is executed the python interpreter jump out of the loop to process the next statement
# break statement is used to bring the control out of the loop when some external condition is triggered
# it terminates the current loop
# that is the loop in which is apears and resumes executions at the next statement immeditely after the end of that loop
# if the break statement is inside a nested loop, the break will terminate the inner most loop

# search whether the number inserted by user is available in the list or not
# a=[1,2,33,6,9,7]
# search=int(input('enter an element to search: '))
# for element in a:
#     if search== element:
#         print('element is found in the list')
#         break
#     else:
#         print('element is not available in the list')
#         break;

# print 10 to 5
# a=10
# while a>=1:
#     print(a)
#     a-=1
#     if a==4:
#         break;
# print('out of the loop')

# using break with string
# a='Atmiya'
# for b in a:
#     print(b)
#     if b=='i':
#         break

# same program as above using while
a='atmiya'
i=0
# while True:
# while 1:
# while 0:
#     print(a[i])
#     if a[i]=='i':
#         break
#     i+=1

# while (i==0):

# break statement in nested loop
# lst=[1,2,3,4,5]
# lst2=[6,7,8,9,10]

# for i in lst:
#     for j in lst2:
#         print(i, j)
#         if i==3 and j==8:
#         if i==7 and j==9:
#         if i==1 and j==6:
#             print('break')
#             break

# a='atmiya'
# for b in a:
#     if b=='m':
#         break

# the continue statement
# a='atmiya university - rajkot'
# for i in a:
#     if i=='a':
#         continue
#     print(i, end="")

# print 1-10, except 5 and 6
# for i in range(1,11):
#     if i==5 or i==8:
#         continue
#     print(i, end=" ") 

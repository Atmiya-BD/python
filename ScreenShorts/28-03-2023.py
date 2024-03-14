# 28-03-2023
# the for loop

# it can be used to execute a group of statements repeteadly depending upon the number of elements in the sequence
# the for loop can work with sequence like string, list, tuple, range etc.
# the first elements of sequence is assigned to the variable is written after 'for' and then the statements are executed. next the second element of the sequcne is assigned to the variable and the statements are executed second time.
# in this way, for each element of the sequence, the statements are executed.
# so the for loop is executed as many times as there are number in the sequence

# syntax:
#     for var sequence:
#           statements

# a='atmiya'
# for ch in a:
#     print(ch)

# display elements of the string using index
# a='atmiya';
# n=len(a)
# for i in range(n):
#     print(a[i])

# display 0-9
# for i in range(10):
#     print(i)

# range start with 0 and end with (n-1)
# display odd number between 1-10
# for i in range(1,10,2):
#     print(i)

# display even number between 1-10
# for i in range(2,10,2):
#     print(i)

# display no from 10 - 1
# for i in range(10,0,-1):
#     print(i)

# printing each elements from the list one by one
# lst=[12,25,2,55.33,"atmiya", [12,3,633.6], ]
# for i in lst:
#     print(i)

# adding all the elements of the list
# lst=[12, 25, 2, 55.33, 25 -96, 45 ]
# sum=0
# for i in lst:
#     sum+=i
# print("sum is=",sum)

# using else with for
# lst=[1,2,5,2,5,22,5]
# for  i in lst:
#     print(i)
# else:
#     print('all the elements of list are printed')

# finding square of each element of the list
lst=[1,2,5,2,5,22,5]
abc=0
n=len(lst)
total=0
for i in range(n):
    # print(lst[i])
    abc=lst[i]**2
    total+=abc
    print(lst[i],"\t",abc)
print('sum of the square is: ', total)



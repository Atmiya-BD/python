# processing the arrays
# the arrays  class of arrays module in python offers methods to process arrays easily.
# the programmers can easily prforms sertain operations by using this methods

# array methods(from screenshots table)

from array import *

ar= array('i', [1,2,3,4,5,6,])
# print("the initial values  inserted in the array: ", ar) 

# appending values to the array
# ar.append(7)
# ar.append(8)
# ar.append(9,10) #invalid task(can take exactly one value at a time)
# print("an array value after the appendings: ", ar)

# insert()
ar.insert(0,11)
# ar.insert(4,44) #first position is index no
ar.insert(44,444) 
ar.insert(4,4444)
# print("an array value after the insert: ", ar)
# if the position specified is not available, than value will be inserted after the last element in the array
# print(ar[44])
# print(ar[7])

# removing the element
# ar.remove(88)
# ar.remove(3)

# removing the last element
# pe=ar.pop()
# print("the poped element was: ",pe)
# print("elements of array after pop: ",ar)

# finding the position of an element
# a=ar.index(4)
# a=ar.index(14)
# print('the position of an element is: ',a)

# removing as per the index/position
# ar.pop()
# print(ar)

# convert an array into a list
# lst=ar.tolist()
# print(lst)
# print(ar)

# taking mark of student, finding total of marks and percentage
# str1=input("enter makrs: ").split(' ')
str1=input("enter makrs: ").split(',')
marks=[int(num) for num in str1]
print(marks)

total=0
for a in marks:
    print(a)
    total+=a

print("total marks: ",total)

l=len(marks)
print("total subjects are: ",l)
print("percentage are: ",total/l)

# convert vs copy
# pop() vs remove()
# insert() vs append()
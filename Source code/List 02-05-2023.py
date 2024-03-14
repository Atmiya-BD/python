#List, Tuple, Dictionary 
# List
#Program to create list using range function #Format of range: range(start, stop, stepsize)

#0-7
# lst1=range (8)#(0:8:1) 
# for i in lst1:
#     print(i, end=' ')
# print()

# lst2=range(8,16)
# for i in lst2:
#     print(i, end=' ')

#odd numbers between 1-10
# print()
# lst3=range (1,10,2)
# for i in lst3: print(i, end=' ')
# print()

#Updating the list
lst4=list(range(1,8))
# print(lst4)

# #Append
# lst4.append(11)
# print(lst4)

# #Update
# lst4[3]=50
# print(lst4)

#Delete by index
# del lst4[3]
# print(lst4)

#Delete by value
# lst4.remove(5)
# print(lst4)

#Finding index of element
# a=lst4.index(2)
# print(a)

#Length of a list
# n=len(lst4)
# print(n)

#Clear the list
# lst4.clear()
# print(lst4)

#Display elements of list in a reverse order
# lst=['sunday', 'monday', 'tuesday']
# a=lst.reverse() #Use of reverse()
# print(a)
# print(lst)

#Concatenation of lists
# a= [1,2,3]
# b=['one', 'two', 'three']
# print(a+b)

#Repetition of list'
# print(a*3)

#Membership in Lists 
# #Using 'in' and 'not in'
# lst=[1,2,3,4,5,6,7]
# a=7
# b=8
# print(a in lst)
# print(b in lst)
# print(a not in lst)
# print(b not in lst)

#Alliasing a list #copy the elements, modification in any list will be done in other list too.
# lst1=[1,2,3,4,5,6,7]
# lst2=lst1 #Aliasing
# print(lst1)
# print(lst2)
# lst2.append(8)
# print(lst1) 
# print(lst2)

#Cloning a list # copy the elements, modification in any list will not effect other list
# lst3=[1,2,3,4,5,6,7]
# lst4=lst3[:]#Cloning
# print(lst3)
# print(lst4)
# lst4.append(8)

#Counting how many times an element is found in the list 
# a=[]
# n=int(input('How many elements to insert?: '))
# for i in range(n):
#     print('Enter the element: ',end='') 
#     a.append(int(input()))
# print('The list is: ',a)
# find=int(input('Enter an element to count: '))
# cnt=0
# for i in a:
#     if(find==i):
#         cnt=cnt+1
# print('{0} is found {1} times.'.format(find, cnt))

#Finding common elements in two lists
# flower1=['rose', 'marigold', 'mogra']
# flower2=['rose','orchid', 'daisy']

#Converting to set
# s1=set(flower1)
# s2=set(flower2)
# s3=s1.intersection(s2)
# print(s3)

#Converting result into list 
# common=list (s3)
# print(common)

#Create nested list
lst=[1,2,3, [10,20]]
print('Elements of list:', lst)
print('The first element of list: ', lst[0])
print('The first element of list: ', lst[3])
for i in lst[0:4]:
    print(i) 
for i in lst[3]:
    print(i)

#Create a list ehich contains square of 1-10 
sqr=[] #Empty list
for i in range(1,11):
    sqr.append
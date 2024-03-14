#The for loop
#Syntax:
	# for var sequence:
	# 	Statements

# a='Atmiya'
# for ch in a:
# 	print('\t',ch)

#Display elements of the string using index
# a='Atmiya'
# n=len(a)
# for i in range(n):
# 	print(a[i])

#Point to remember

#Display 0-9
# for i in range(10):
# 	print(i)

#Display odd numbers between 1-10
# for i in range(1,10,2):
# 	print(i)

#Display even numbers between 1-10
# for i in range(2,11,2):
# 	print(i)

#Display numbers from 10-1
# for i in range(10,0,-1):
# 	print(i )

#Printing each elements from the list one by one
# lst=[2,3,5,10.1,'a','Atmiya']
# for i in lst:
# 	print(i)

#Adding all the elements of the list
# lst=[2,3,5,10,5,8,9,10]
# sum=0
# for i in lst:
# 	print(i)
# 	sum=sum+i
# print('Sum=',sum)

#Using else with for
# lst=[2,3,5,10.1,'a','Atmiya']
# for i in lst:
# 	print(i)
# else:
# 	print('All the elements of list are printed')

# #Finding square of each element of the list
# lst=[2,3,5,10,5,8,9,10]
# abc=0
# n=len(lst)
# #print(n)
# for i in range(n):
# 	print(lst[i])
# 	abc=lst[i]**2
# 	print('\t',abc)

lst=[2,3,5,10,5,8,9,10]
abc=0
defg=0
n=len(lst)
#print(n)
for i in range(n):
	#print(lst[i])
	abc=lst[i]**2
	defg=defg+abc
print(defg)
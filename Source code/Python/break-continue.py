#Break and Continue
#Search whether the number inserted by user is available in the lust or not
# a=[1,2,3,4,5]
# search=int(input('Enter an element to search: '))
# for element in a:
# 	if search==element:
# 		print('Element is found in the list')
# 		break
# else:
# 	print('Element is not available in the list')

#Print 10 to 5
# a=10
# while a>=1:
# 	print(a)
# 	a=a-1
# 	if a==5:
# 		break
# print('Out of the loop')

#Using break with string
# a='Atmiya'
# for b in a:
# 	print(b)
# 	if b=='m':
# 		break

#Same program as above using while
# a='Atmiya'
# i=0
# while True:
# 	print(a[i])
# 	if(a[i]=='y'):
# 		break
# 	i=i+1

#Break statement in nested loop
# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# for i in l1:
# 	for j in l2:
# 		print(i,j)
# 		if i==1 and j==6:
# 			print('Break')
# 			break

#The Continue statement
# a='AtmiyaUniversityRajkot'
# for i in a:
# 	if i=='a':
# 		continue
# 	print(i,end='')

#Print 1-10, except 5 and 6
for i in range(1,11):
	if i==5 or i==9:
		continue
	print(i,end='')
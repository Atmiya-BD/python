# Syntax:
# 	while condition:
# 		statements
# a=1
# while a<=10:
# 	print(a)
# 	a=a+1 #a+=1
# print('End of while')

#Allowing user to enter numbers, as soon as he insert 0, program will give sum of all the entered numbers
# total=0
# number=int(input('Enter a number: '))
# while number !=0:
# 	total=total+number
# 	number=int(input('Enter a number: '))
# print('The sum of entered numbers: ',total)

#Table of 1
# num=int(input('Enbter the number for whih you want a table: '))
# counter=1
# while counter<=10:
# 	ans=num*counter
# 	print(num,'x',counter,'=',ans)
# 	counter=counter+1

#Program to display even numbers between 1 and 10
# a=1
# while a>=1 and a<=100:
# 	print(a)
# 	a=a+2

#Even or Odd based on users choice(1 for odd, 2 for even)
# num=int(input('Enter your choice from either 1 or 2: '))
# if num==1:
# 	print('Program will print odd numbers between 1-10')
# 	while num>=1 and num<=10:
# 		print(num)
# 		num=num+2
# elif num==2:
# 	print('Program will print even numbers between 1-10')
# 	while num>=2 and num<=10:
# 		print(num)
# 		num=num+2
# else:
# 	print('Enter either 1 or 2')

#Program to find and display only even numbers from the given set of numbers
# a=[2,45,6,7,5,57,5,45]
# b=0
# while (b<len(a)):
# 	if a[b]%2==0:
# 		print(a[b])
# 	b=b+1

#Accept string from the user and print each character one by one
a='Atmiya'
b=0
while(b<len(a)):
	print(a[b])
	b=b+1
#if...elif...else

#Syntax:
# 	if condition:
# 		statements1
#	elif condition:
# 		statements2
# 	elif condition:
# 		statements3
#  	else:
#  		statements4

#Program to know whether the given number is positive, negative or zero
# a=int(input('Enter the number: '))
# if a>0:
# 	print(a, 'is a positive number')
# elif a==0:
# 	print('It is zero')
# else:
# 	print(a, 'is a negative number')

#A program to print the entered number into words
# a=int(input('Enter the number: '))
# if a==0:
# 	print('Zero')
# elif a==1:
# 	print('One')
# elif a==2:
# 	print('Two')
# elif a==3:
# 	print('Three')
# elif a==4:
# 	print('Four')
# elif a==5:
# 	print('Five')
# else:
# 	print('The range is between 0 and 5')

#Discount (0,5000,5000+10,8000+12,10000+15,20000+25)
# amount=int(input("Please enter the amount: "))
# if amount<=0:
# 	print('Bill amount must be more than 0')
# elif amount<=5000:
# 	print('Purchase little more to avail discount')
# elif amount>=5000 and amount<=8000:
# 	print('You got 10 percent discount')
# elif amount>=8000 and amount<=10000:
# 	print('You got 12 percent discount')
# elif amount>=10000 and amount<=20000:
# 	print('You got 15 percent discount')
# elif amount>20000:
# 	print('Hurray! you got a maximum discount of 25 percent')

#Result
# marks=int(input('Enter your marks: '))
# if marks<50:
# 	print('You need to re-appear the exam')
# elif marks>=50 and marks<60:
# 	print('You passed the exam')
# elif marks>=60 and marks<70:
# 	print('You passed the exam with First class')
# elif marks>=70 and marks<80:
# 	print('You passed the exam with Distinction')
# elif marks>=80 and marks<=100:
# 	print('You passed the exam with Honors')
# else:
# 	print('Enter Valid marks')

#Discount (0,5000,5000+10,8000+12,10000+15,20000+25)
# amount=int(input("Please enter the amount: "))
# if amount<=0:
# 	print('Bill amount must be more than 0')
# elif amount<=5000:
# 	print('Purchase little more to avail discount')
# elif amount>=5000 and amount<=8000:
# 	print('You got 10 percent discount')
# 	discount=(amount*10)/100
# 	print('You got discount of', discount)
# 	payable=amount-discount
# 	print('You have to pay', payable)
# elif amount>=8000 and amount<=10000:
# 	print('You got 12 percent discount')
# 	discount=(amount*12)/100
# 	print('You got discount of', discount)
# 	payable=amount-discount
# 	print('You have to pay', payable)
# elif amount>=10000 and amount<=20000:
# 	print('You got 15 percent discount')
# 	discount=(amount*15)/100
# 	print('You got discount of', discount)
# 	payable=amount-discount
# 	print('You have to pay', payable)
# elif amount>20000:
# 	print('Hurray! you got a maximum discount of 25 percent')
# 	discount=(amount*25)/100
# 	print('You got discount of', discount)
# 	payable=amount-discount
# 	print('You have to pay', payable)
#if vs. elif
#(Using if) Accept marks from 4 students, display which mark is highest among all.
# std1=int(input('Please enter marks of Student 1: '))
# std2=int(input('Please enter marks of Student 2: '))
# std3=int(input('Please enter marks of Student 3: '))
# std4=int(input('Please enter marks of Student 4: '))
# if std1>std2 and std1>std3 and std1>std4:
# 	print('Student 1 got the highest marks')
# if std2>std1 and std2>std3 and std2>std4:
# 	print('Student 2 got the highest marks')
# if std3>std1 and std3>std2 and std3>std4:
# 	print('Student 3 got the highest marks')
# if std4>std1 and std4>std2 and std4>std3:
# 	print('Student 4 got the highest marks')
# else:
# 	print('Please enter valid marks')

#(Using if...elif...else) Accept marks from 4 students, display which mark is highest among all.
# std1=int(input('Please enter marks of Student 1: '))
# std2=int(input('Please enter marks of Student 2: '))
# std3=int(input('Please enter marks of Student 3: '))
# std4=int(input('Please enter marks of Student 4: '))
# if std1>std2 and std1>std3 and std1>std4:
# 	print('Student 1 got highest marks')
# elif std2>std1 and std2>std3 and std2>std4:
# 	print('Student 2 got highest marks')
# elif std3>std1 and std3>std2 and std3>std4:
# 	print('Student 3 got highest marks')
# elif std4>std1 and std4>std2 and std4>std3:
# 	print('Student 4 got highest marks')
# else:
# 	print('Please enter valid marks')

#(Using nested if) Accept marks from 4 students, display which mark is highest among all.
# a=80
# b=45
# c=90
# d=85
# if(a>b):
# 	if(a>c):
# 		if(a>d):
# 			print('A is highest')
# if(b>a):
# 	if(b>c):
# 		if(b>d):
# 			print('B is highest')
# if(c>a):
# 	if(c>b):
# 		if(c>d):
# 			print('C is highest')
# if(d>a):
# 	if(d>b):
# 		if(d>c):
# 			print('D is highest')

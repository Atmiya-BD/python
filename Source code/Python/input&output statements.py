#Input statements
# a=input()
# print(a)
#with the message
# name=input('Enter your name')
# print(name)
#Restricted entry
# no=int(input('Enter the number'))
# print(no)
# no=float(input('Enter the number'))
# print(no)
#Only the first character will be displayed
# char=input('Enter the character: ')[0]
# print(char)
#Adding two values by taking from user using .format
# a=int(input('Enter the first value: '))
# b=int(input('Enter the second value: '))
# print('The sum of {0} and {1} is {2}'.format(a,b,a+b))
#Adding and finding the product of two values by taking from user using .format
# a=int(input('Enter the first value: '))
# b=int(input('Enter the second value: '))
# print('The sum of {0} and {1} is {2} and the product of {0} and {1} is {3}'.format(a,b,a+b,a*b))

#Use of split() method
# a=[a for a in input('Enter the strings:').split()]
# print(a)

# no1,no2,no3=[int(no)for no in input('Enter three numbers: ').split()]
# print('The sum of three numbers are: ',no1+no2+no3)

# no1,no2,no3=[int(no)for no in input('Enter three numbers: ').split(',')]
# print('The sum of three numbers are: ',no1+no2+no3)

#Use of eval() function
# a,b=7,16
# ans=eval("a+b+3")
# print(ans)
#Using eval() along with input(), taking expression from the user.
# a,b=7,16
# ans=eval(input("Enter an expression"))
# print('The result of your expression is: %d'% ans)

a=eval(input('Enter the values in list: '))
print("values in the list are: ",a)
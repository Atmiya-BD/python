 #Input and output statements
# #Output Statements
# #The print()statement
# print()

# #The print("string") statement
# print('Atmiya')
# print("This is a \n new line")
# print("The tab is \tis used here")

# print("The city is"+"Rajkot")

# #The print(variables list) statement
# a,b=7,16
# print(a,b)
# print(a,b,sep=",")

# print('Atmiya')
# print('University')
# print('Rajkot')

# print('Atmiya',end='\t')
# print('University')
# print('Rajkot')

# #The print(object) statement
# a=[7,'Atmiya','Rajkot']
# print(a)

# #The print("String", variables list) statement
# a=7
# print(a,"The value is printed here")
# print("User have entered",a, "as an input")

#The print(formatted string) statement
a=7
print('Value is %i' % a)

a,b=10,16
print('a is %i b is %i'%(a,b))
a,b=10,16
print('a is %i b is %i'%(b,a))

university="Atmiya"
print('Hi %s'%university)
print('Hi %20s'% university)
print('Hi (%-20s)'% university)

print('The first character is %c,and the second character is %c'%(university[0],university[1]))

num=123.456789
print('The number is %f'%num)
print('The number is %6.2f'%num)

#Inside the formatted string
no1,no2,no3=1,2,3
print('The first number is {0}, the second number is {1}, and the third number is {2}'.format(no2,no3,no1))
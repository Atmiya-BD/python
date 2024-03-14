#input and output statements

# the data given to this computer is called input. the result return by the computer are called output. so we can say that a computer take input and process that input and produce the output

#output statements
# the output in python is displayed using the print function. the print function can be used in different formats

#the print() statements

# when the print function is called, simply it will throught coursour to the next line it means a blank line will be displayed

# the print("string") statement

# the string represent a group of characters when a string is passed to the print function,  the string is displayed as it is

# EX: 
print('atmiya')

# NOTE: note that single quotes or double quotes have the same mining

# we can use escape sequences characters inside the print function

print("this is a \n new line")

print("the tab is \t is used here ")

# the plus operator is used with number will add both numbers but when used with strings it will works as concenation operator. it will jon string

print("the city is " + "Rajkot ")

#the print(variables list) statements

# we can also display the values of the variables using the print function
a,b=7,16
print(7,16)

# we can seperate the string using 'sep' attribute
print(7,16, sep=",")
print(7,16, sep="-")

# each print function throught the function to the next line after displaying output
print('atmiya')
print('university')
print('rajkot')

# we can use "end" attribute as below

print('atmiya', end="\t")
print('university')
print('rajkot')

#the print(object) statement
a=[7, 'atmiya', 'rajkot'];
print(a)

#the most common use of the print function is to use strings along with variables inside the print function
#the print("string", variables list) statement

a=7
print(a, "the value is printed here")
print("user have entered:", a," as an input")

#the print(formatted string) statement
# we can fromat the output using the print function. for that purpose, the special operator '%' is used to joint string with a variable. we can use %i, or %d to represent decimal integer number we can use %f to represent float value we can use %s to represent string 

a=8
print("value is %i"%a)

a,b=10,16  
print("a is %i b is %i "%(a,b))

a,b=10,16  
print("a is %i b is %i "%(b,a))


university="atmiya"
print('hi %s'%university)
print('hi %20s'%university)
print('hi (%-20s)'%university)

print('the first character is %c, and the second character is %c'%(university[0], university[1]))

num=1254.3363222
print('the num is %f'%num)

print('the num is %6.2f'%num)
#total 6, in them 2 decimal

#inside the formatted string
no1, no2, no3=1,2,3
print("the first number is {1}, the second number is {0}, the third number is{2}".format(no2, no3, no1))




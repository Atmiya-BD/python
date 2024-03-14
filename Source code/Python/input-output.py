# the data given to the computer is called a input.
# the result return by the computer are called output.
# so we can say that a comuter tack input, processes that inputs and produces the output

# ->output statements:
# the output in python is displayed using the print() function the print function can be used in different formats.

# the print() statements:
# when the print function is called simply, it will throw the curser to the next line. it means that a blank line will be displayed.
	
# ex = print()
# print(ex)

# the print("string") statements:	
# string represents a group of characters. when a string is passed to the print function, the string is displayed as it is.
# note that or have the same meaning.

# we can use escape sequence charcter inside the print function

# + operator:
# when used with numbers will add both numbers but when used with strings it will work as concatination operator. it will join two strings.

# print(variable lists) statements:

# 	we can also displayes the value of variables using the print function
# a,b = 7,45;
# print(a, b)
# print(a, b, sep=",")

# we can seprate the string using the 'sep' attribute. in each print function throws the curser to the next line after displaying the output.

# we can use 'and attribute', as below,
# print('atmiya',end='\t')
# print('university')
# print('rajkot')

# print(object) statements:
# the most common use of the print function is to use strings along with variables inside te print function.
# a=7
# print(a,"the value is printed here")
# print("user have entered",a,"as an input")

# print(formatted string) statements :
# we can format the output using the print function. for that purpose the special operator'+' is used.
# it joins string with a variable. we can use %i or %d to represent decimal
# integer we can use %f for floating values. we can use %s for strings

# a=7
# print('value is %i' %a)

# a,b=10,12
# print('a is %i b is %f'%(a,b))

# a,b=10,12
# print('a is %i b is %d'%(a,b))

# university="atmiya"
# print('hi%s'%university)
# print('hi%20s'%university)
# print('hi(%-20s)'%university) # it give space from the negative index
# print('the first character is %c, and the second character is %c'%(university[0],university[1]))

# num=123.456789
# print('number is %f'%(num))
# print('number is %6.2f'%(num))

# inside the formatted string
# no1,no2,no3=1,2,3
# print('number is: {0}, the number is: {1}, the number is: {2}, and the third number is: {3}'.format(no1, no2, no3, no1))
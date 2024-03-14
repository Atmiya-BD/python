# s1='Welcome to Atmiya University, Rajkot' #Both s1 and s2 will have same output
# s2="Welcome to Atmiya University, Rajkot" #Both s1 and s2 will have same output
# s3='Welcome to "Atmiya University", Rajkot' #To have quote in the output
# s4='Welcome to \t Atmiya University, \nRajkot' #To give tab and print on new line (escape character)
# s5=r'Welcome to \t Atmiya University, \nRajkot' #r is used to nulify the effect of escaper character

# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(s5)

# s6=u'\u7770' #Unicode
# print(s6)

# print(len(s1)) #To find no of characters in the string

# s7="atmiya"
# s8="University"

# s=s7+s8 #String Concatenation
# print(s)

#A program to access each element of a string in forward and reverse order (using While) 
# str='Atmiya University'
# n=len(str)
# i=0
# while i<n:
#     print(str[1], end=' ')
#     i=i+1
# print()

#In the reverse order
# n=len(str)
# while i<=n: 
#   print(str[-i], end =' ') 
#   i=i+1

# #A program to access each element of a string in forward and reverse order (using for loop) 
# str='Atmiya University'
# i=0
# for i in str: 
#   print(i, end=' ')

# #Reverse
# for i in str[::-1]: 
#   print(i, end='|')

# #Slicing
# str='Atmiya'
# print(str[0:6:1]) #[:::]
# print(str[0:6:2])
# print(str[-1::-1])

#Checking whether string exist in the main string 
# str=input('Enter the string: ')
# substr=input('Enter the seach string: ') 
# if substr in str:
#     print(substr, 'is availabe in the main string')
# else:
#     print(substr, 'is not available in the main string')

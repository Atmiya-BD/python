# counting sub-string in string
# format: stringname.count(substring, beg, end)

# finds in given range
# str="new india new dreams"

# n=str.count('new', 0,20)
# n=str.count('new')
# n=str.count('new', 5 , 10)
# print(n)

# replacing a string
# str="good morning"
# s1="morning"
# s2="evening"

# str=str.replace(s1, s2)
# print(str)

# changing case of a string
# str="Your Future is Bright"

# print(str.upper())
# print(str.lower())
# print(str.swapcase())
# print(str.title())

# string testing methods
# (screenshot)

# mobile_number=input("Enter Mobile Number: ")
# print(mobile_number.isdigit())

# if mobile_number.isdigit()!=True:
#     print("enter valid mobile number")

# sort a string into alphabet order
# str=[]
# n=int(input("how many strings you want to enter: "))
# for i in range(n):
#     print("enter the string: ", end="")
#     str.append(input()) #use of append method
# print(str)

# str.sort() #use of sort method
# print(str)

# for i in str:
#     print(i)

# ---------------------------------------------

# program to search the strings from the group of strings and also find its position
# str=[]
# n=int(input("how many strings you want to enter: "))
# for i in range(n):
#     print("enter the string: ", end="")
#     str.append(input()) #use of append method
# print(str)

# ask user for the string to search
# srch=input("Enter the string to search: ")
# # searching
# for i in range(len(str)):
#     if srch==str[i]:
#         print("the search string found at the position: ", i)
#         break
#     else:
#         print("the searched string not found")

# flag=False

# searching
# for i in range(len(str)):
#     if srch==str[i]:
#         print("the search string found at the position: ", i)
#         flag=True

# if not flag:
#     print("the searched string not found")

# ---------------------------------------------

# working with characters 
# str="atmiya"
# # ch=str[0]
# # ch=str[4]
# ch=str[0:3]
# print(ch)

# program to know the the type of character
str=input("enter a character: ")
ch=str[0]
if ch.isalpha():
    print("it is an alphabet")
    if ch.isupper():
        print(" alphabet is upper case")
    else:
        print(" alphabet is lower case")
else:
    print("it is number")

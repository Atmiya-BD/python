# try:
#     print("you are in the try block")
#     a=int(input("enter a value:"))
#     b=int(input("enter a value:"))
#     c=a/b

# except:
#     print("you are in except block")
#     print("number cannot be divide with 0")

# else:
#     print("you are in else block")
#     print("the answer of division is ", c)
# finally:
#     print("you are in finally block")

# type of exception (built in exception)
# handling multiple exceptions in one try 
# def avg(list):
#     total=0
#     for i in list:
#         total=total+i
#     average = total/len(list)
#     return average, total

# call the function
# try:
#     tot, avg =avg([1,2,3,4,5,6,7,8,9,'a'])
# except TypeError:
#         print("you are not in the try block")

# except ZeroDivisionError:
#         print("you are not in the try block")

# handling multiple exceptions in one try 
# def avg(list):
#     total=0
#     for i in list:
#         total=total+i
#     average = total/len(list)
#     return average, total

# # call the function
# try:
#     tot, avg =avg([1,2,3,4,5,6,7,8,9,0,'a'])
# except (TypeError,ZeroDivisionError):
#     print("please provide number only")
    
# try:
#     tot, avg =avg([1,2,3,4,5,6,7,8,9,0,'a'])
# except (TypeError,ZeroDivisionError):
#     if TypeError:
#         print("please provide number only:)")
#     elif ZeroDivisionError:
#         print("please provide number greatern then 0")

# the assert 
# the assert statement is useful to ensure that given condition is true if it is not true it raises an 

# AssertionError
# syntax:
#     assert condition message[message not mandatory]

# assertion method can be written in two ways:
    # 1. if the condition is false then the exception by the name AssertionError is raised along with the message written in the assert statement
    #  2. if the error message is not returned then the AssertionError without the message will be displayed

# handle assertion errors
# assertion without an error message
# try:
#     a=int(input("enter a number between a and 10: "))
#     assert a>=1 and a<=10
#     print("the entered number is: ",a)

# except:
#     print("the number is not between 1 and 10")

# assertion without an error message
# try:
#     a=int(input("enter a number between a and 10: "))
#     assert a>=1 and a<=10, "the number is not between 1 and 10"
#     print("the entered number is: ",a)

# except AssertionError as obj:
#     print(obj)

# user defined exception(custom exception)
# version-1
# def validate(name):
#     if len(name) <10:
#         raise ValueError

# version-2
# def validate(name):
#     if len(name) <10:
#         raise ValueError('name is shorter than required')

# version-3
# class NameShorter(ValueError):
#     pass

# def validate(name):
#     if len(name) <10:
#         # raise NameShorter
#         raise NameShorter('name is shorter than required')

# version-4
# def validate(name):
#     try:
#         if len(name) <10:
#         # raise NameShorter
#             raise NameShorter('error')
#     except(NameShorter):
#         print('name is shorter than required')

# callint the function
# validate("abc")

# final version
# class BirthYear(OSError):
#     pass

# year=int(input("enetr your birth year: "))
# your_age=2023-year
# print("your age is: ",your_age)

# try:
#     if your_age<=30 and your_age>20:
#         print('you can apply for the job')
#     else:
#         raise BirthYear
# except BirthYear:
#         print('your age is not as required')

# file handling
# types of files
    # in python there are two types of files
    # 1. text files
    # 2. binary files

    # text files store the data in the form of the characters. For example if we store student name 'abc', it will be stored as three characters and it score is 87 it store it as two characters.normally text file are use to store character or string
    
    # binary files store entire data in the form of bytes that is i.e. a group of 8 bits each. when the data is retrived from the binary file, the programmer can retrieve the data as bytes. binary files can be used to store text, images, audio and video files

# opening & closing file 
# we should use open() function to open a file. this function accepts 'filename' and open mode in which to open the file

# syntax:
#     file handler = open('filename', 'open mode')

# file opening mode
    # 1. -w (to write data into a file. if any data is already present in the file, it would be deleted and the present data will be stored)
    # 2. -r (to read data from the file. the file pointer is placed at the beginning of the file )
    # 3. -a (to append data to the file. appending at the end of the existing data. file pointer placed at the end of the file. if the file is not present it will be created)
    # 4. -x (to open the file in the exclusive creation mode. the file creation is fails if the file already exists)
    
    # 5. + (+with  'w','r','a' will allow both reading and writing)
    
# diff -r(starting position) vs -a(end of the content)

# closing the file
    # a file which is opened should be closed using the close() method. if the file is not closed then data may get currept or be may loss data.
    # alos if file not closed then it may not free the memory till the file is open
    # we can close file using f.close()

# program to create a text file and store data
# creating a file to store characters
# open the file for writing data

f=open("mytest.txt", 'w')
print(type(f))

# accept text from the user
str=input('enter the test: ')

# writing string into the file
f.write(str)

p=f
print(type(p))
# closing the file
f.close()
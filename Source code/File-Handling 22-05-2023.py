# file handling
# types of files
# file handler=open("filename", "open mode")
# file opening mode
# closing the file
# close()

# programt to create text file and store data
# creating a file to store characters
# open the file for writing data
# f=open('test.txt','w')
# # accept text from the user
# str=input('enter the text: ')
# # writing string into the file
# f.write(str)
# # close the file
# f.close()

# ex:-2
# f=open('test.txt','r')
# str=f.read()    #reading the content of file
# print(str)  #display the content on the screen
# f.close() #close the file

#creating a file to store group of strings into a text file
# f=open('myyfile.txt','w')
# print("enter text you want to enter in the file: ")
# while str!='$': # stop accepting the string when $ is pressed
#     str=input() #accept string into str
#     if(str!='$'):
#         f.write(str+'\n')
# f.close()

# appending data into the existing file
# f=open('myyfile.txt','a')
# print("enter text you want to enter in the file: ")
# while str!='$': # stop accepting the string when $ is pressed
#     str=input() #accept string into str
#     if(str!='$'):
#         f.write(str+'\n')

# reading the file 
# f=open('myyfile.txt','r')
# str=f.read()
# print(str)
# f.close()

# checking whether file exixt of not
# the operating system(OS) module has sub module by the name 'path' that contains a method isfile() 
# this method can be used to know wheter a file that we are opening really exists or not
# syntax:
#   os.path.isfile(file_name)
# 
#  it gives true if files exists otherwise false

from asyncio.windows_events import NULL
import os,sys
# fname=input("enter the file name to open:")
# if os.path.isfile(fname):
#     # f.open(fname+'does exists' )
#     print(fname+' does exists')
# else:
#     print(fname+' does not exists')

# print(os.path.isfile('test.txt'))

# counting number if lines, words, and characters if the file is available
# fname=input("enter the file name: ")
# if os.path.isfile('test.txt'):
#     f=open(fname,'r')
#     cl=0    #cl=cw=cc=0
#     cw=0
#     cc=0

#     # reading lines form the file
#     for line in f:
#         words=line.split()
#         cl=cl+1
#         cw=cw+len(words)
#         cc=cc+len(line)

#     print('number of lines in a file is: ', cl)
#     print('number of wrods in a file is: ', cw)
#     print('number of characters in a file is: ', cc)
#     f.close()
# else:
#     print(fname+' does not exists')

# working with binary files
# binary files handle data in the form of bytes
# it can store files like text, image, audio or video
# to open a binary file for reading purpose we can use 'rb' 
# similarly to write bytes into binary file we can use 'wb'
# to read bytes form binary file we can use the read() method and to write bytes in to a binary file we can use the write() method

# to copy an image file into another file 
# f1=open('index data.png','rb')
# f2=open('test.png','wb')

# bytes=f1.read()
# f2.write(bytes)

# f1.close()
# f2.close()

# the 'with' statement
# the 'with' statment can be used while opening the file 
# the advantage of 'with' statemnt is that it will take care of closing a file which is opened by it
# the format of using 'with' statement is 
    # with open('file.txt', 'openmode') as fileobject:

# the seek() and tell() methods
# we can use tell() method the know the position of the file pointer
# it returns the current position of the file pointer from the beginning of the file
# it is used in the form
# syntex of tell()
#     n=f.tell()

# if you want ot move the file pointer to another position, we can use the seek() function 
# it is used in the form 
# syntax of seek()
    # f.seek(offset,fromwhere)

# here 'offset' represents how many bytes to move, 'fromwhere' represent from which position to move
# for example: 'fromwhere' can be 0,1 or 2
# here 0 represents from the beginning of the file
# 1 represents from the current position 
# 2 represents from the ending of the file
# the default values is 0

# taking data from the user and store in the form of binary file
# reclen=15
# # open the file in 'wb' mode
# with open('st.bin','wb') as fp: #use of 'with' will take care of closing the file
#     n=int(input('how many you want to enter? '))
#     for i in range(n):
#         stationary=input('enter the name of item: ')
#         ln=len(stationary) #to find the length of entered item
#         # to add number of spaces at the end to make it of 15 characters
#         # stationary=stationary+(reclen-ln)*' '
#         stationary=stationary.encode() #encode() converts the string in binary
#         fp.write(stationary)

# to read the file by taking record number from the use 
# reclen=15
# with open('st.bin','rb')as fp:
#     n=int(input('enter the record number to search: '))
#     fp.seek(reclen*(n-1)) #moves the file pointer to end of n-1
#     str=fp.read(reclen) #get the nth record with 15 characters
#     print(str.decode()) #decode() converts the binary to string
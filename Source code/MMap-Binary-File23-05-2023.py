# rando, accessing of binary file using mmap

# the fullform of mmap keys 'memory mapped file'
# once a binary file is created with some data with, that data is viewed as viewed as strings and it can be manipulated using mmap module
# the mmap can be used as 
    # syntax: mm=mmap.mmap(f.fileno(),0) 
# this will map the currently opened file 'f' with the file object 'mm'
# the 'f' represents the actual binary file that is being mapped 
# the secodn argument is 0, it means the whole file should be for mapping
# with open("phonebook.dat", "wb") as fp:
#     n=int(input("how many records to enter:?"))
#     for i in range(n):
#         name=input('enter your name: ')
#         phone=input('enter number: ')
#         name=name.encode()      #converting name form string to bytes
#         phone=phone.encode()      #converting phone form string to bytes
#         fp.write(name+phone)     #writting data to the file

# performing various operations on a binary file
# import mmap,sys

# print('1 to view all the entries')
# print('2 to phone numbers')
# print('3 to modify an entries')
# print('4 exit')

# ch=input('enter your choice: ')
# if ch=='4':
#     sys.exit()

# with open("phonebook.dat", 'r+') as f: #opening the binary in both read and write mode
#     mm=mmap.mmap(f.fileno(), 0) #map the file using mmap, 0 means the whole files
#     if(ch=='1'): #display the entire file
#         print(mm.read().decode())

#     if(ch=='2'): #display phone number        
#         name=input('enter name: ')
#         n=mm.find(name.encode()) # returns the position of the name in the file
#         n1=n+len(name) #go to end of name
#         ph=mm[n1:n1+10] #used the concept of sliciing) display the next 10 bytes
#         print('phone no is: ',ph.decode())

#     if(ch=='3'): #modify an entry        
#         name=input('enter name: ')
#         n=mm.find(name.encode()) # returns the position of the name in the file
#         n1=n+len(name) #go to end of name
#         ph1=input('enter new phone number: ') #taking new phone number
#         mm[n1:n1+10]=ph1.encode()  #the old phone no is 10 bytes after n1 
# mm.close()

# zipping the contents of files
# from zipfile import *; #importing the zipfile module
# # creating the zip file
# f=ZipFile('sample.zip', 'w', ZIP_DEFLATED) # either you can use ZIP_STORED

# # adding files to be zipped
# f.write('phonebook.dat')
# # f.write('phonebook1.dat')

# # close the zip file
# f.close()

# ONLY ZIP & ZIP WITH COMPRESS

# to unzip the file
# from zipfile import *
# z=ZipFile("sample.zip", "r")
# z.extractall("D:\\exam")
# z.extract("D:\\exam")
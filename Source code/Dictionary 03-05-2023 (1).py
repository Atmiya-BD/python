# dictionary
# a dictionary represents a group of elements arrange in the form of key-values pairs
# in the dictionary, first element is considered as 'key' and imdiate next is considered as its 'value'
# we can not use slicing or indexing to retrive elements to dictionary

# dt={    1: "abc",     2: 'pqr',    3: "xyz" }
# print(dt)

# operations on dictionaries:
# dt={    'name': "chagan",     'id': "101",    'salary': 15000 }
# print(dt)
# print('the id of employees is: ', dt['id']) #retriving values using key
# print('the salary of employees is: ', dt['salary']) #retrieving values using key

# n=len(dt) #returns no of key value pair
# dt['salary']=52000 #updating the value using key
# dt['dept']="MCA" #adding new key: value
# del dt['id'] #deleting a pair of key:value
# print(dt)

# print('id' in dt)
# print('dept' in dt)

# print('id' not in dt)
# print('dept' not in dt)

# dictionary methods
# dt={'name': "chagan", 'id': "101", 'salary': 15000 } #creating dictionary 
# print(dt)

# dict=dt.copy() #copys the content of dt to dict
# print('the values of dict:', dict)

# a=dict.keys() #to retrieve all the keys from the dictionary
# a=dict.values() #to retrieve all the values from the dictionary

# print(dict.get('name')) #displaying the value of specified key
# print(dict.get('id'))
# print(dict.items()) #returns a list containing a tuple for each key value pair

# print(dict.pop('id')) #pops the value associated with key
# print(dict)

# print(dict.clear()) #removes the all the keys and values, means empty the dictionary

# print(dict)
# print(type(dict))

# program to take subject and makrs from student and display total marks, display the marks of entered subject
# marks={}
# print('how many subjects you want to enter: ',  end="")
# n=int(input(''))
# for i in range(n):
#     print('enter subject name: ')
#     key=input()
#     print('enter mark: ')
#     val=int(input())
#     marks.update({key:val})
# print(marks)

# total=sum(marks.values())
# print('total marks are: ',total)

# print('enter name of subject to know it marks: ')
# sub=input('')
# mar=marks.get(sub,-1)
# if mar==-1:
#     print('invalid subject')
# else:
#     print('the makrs in {} are {}'.format(sub, mar))

# mar=marks.get(sub)
# if mar==None:
#     print('invalid subject')
# else:
#     print('the makrs in {} are {}'.format(sub, mar))

# sorting the elements of a dictionary using lambda function
# a lambda is function that does not have a name and can be written without 'def' keyword
# they are used to perform some calculation or processing easily

# a=lambda x,y: x+y
# print(a(10,20))

# there are two arguments in the function named x & y, after colon(:) we wrote the body i.e.(that is) x+y, and this is the value returned by the lambda function

colors={9:'blue', 7:'red', 2:'green', 4:'yellow'}
c1=sorted(colors.items(), key=lambda a:a[0]) #sorting on the basis of the key using lambda function
print(c1)
c1=sorted(colors.items(), key=lambda a:a[1])  #sorting on the basis of the key using lambda function
print(c1)


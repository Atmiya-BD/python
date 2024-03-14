# 5). Create a dictionary with at least 10 values and perform the following task:
mydict={
    'rollno':"10",
    'fname':"abc",
    'lname':"pqr",
    
    'contacts':"963254100",
    'email':"abc@example.com",
    'college':"atmiya university",
    
    'addresses':"kalavad road",
    'city':"rajkot",

    'car':"Thar",
    'phone':"iphone 13 pro max"
}

# -Display all the elements of the dictionary.
print(mydict)

# -Check the class of the dictionary you made.
print(type(mydict))

# -Display the value stored in the key 7.
print(mydict['addresses'])
# print(mydict[7])

# -Change the value stored in the key 7.
print("before updating : ",mydict['addresses'])
mydict['addresses']='University Road, rajkot'
print("after updating : ",mydict['addresses'])

# -Display all the values only.
print(mydict.values())
# print(mydict.keys())
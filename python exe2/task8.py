# 8). Create a bytes and perform the following tasks:
mylst=[10,55,63,9,6,203 ]
# print(mylst)

mylst=bytes(mylst)
print(mylst)
# print(type(mylst))

# -Display the first element using negative index.
print(mylst[-6])

# -Display the last element using positive index.
print(mylst[5])

# -Add two values in to it.
# we can not modify any element from bytes


# -Modify the last element.
# we can not modify any element from bytes
# b[a]=8 #this is not allowed in byte
# 'bytes object doesnot support item assignment'



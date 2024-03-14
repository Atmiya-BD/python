# 1 Create a list using range function and do following activities: append some value, update some value, Delete the value (by position and by value)

lst=[a for a in range(10,20)]
print(lst)

# append values 
lst.append(111)
print(lst)

# insert value on specific index
lst.insert(3, 55)
print(lst)

# update the value on specific index
lst[1]="abc"
print(lst)

# delete from specific index
del lst[2]
print(lst)

# delete from last
lst.pop()
print(lst)
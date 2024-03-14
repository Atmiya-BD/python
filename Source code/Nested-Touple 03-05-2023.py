# nested tuples

# tpl=(10,20,30,(40,50))
# print (tpl)
# print (tpl[3])

# taking details of employees in tuple and sort it
# emp=((2,"abc", 3000),(1,"jk", 20000),(3,"dk", 1000))

# print (emp)
# print (emp[2])
# print (sorted(emp))

# sorting on the basis of employee names
# print (sorted(emp,key=lambda emp: emp[1]))

# sorting on the basis of employee salary
# print (sorted(emp,key=lambda e: e[2]))
# print (sorted(emp,key=lambda e: [2]))

# -------------------------------------------------------

# inserting elements in a tuple
# names=('a','b','d','e','f')
# print (names)

# enter new name to insert and position at which to be entered
# lst=[input("Enter new value: ")]
# new_nm=tuple(lst)
# print (new_nm)
# pos=int(input('enter the position: '))

# copy names from 0th position to pos-1
# temp_name=names[0: pos-1] #[start: stop]
# print (temp_name)

# temp_name=temp_name+new_nm
# print (temp_name)

# concatenate remaining elements of names from pos-1 till end
# names=temp_name+names[pos-1: ]
# print (names)

# ------------------------------------------------------

# modify elements in the existing tuple
# insert vs modify 
# names=('a','b','d','e','f')
# print (names)

# enter new name to insert and position at which to be entered
# lst=[input("Enter new value: ")]
# new_nm=tuple(lst)
# print (new_nm)
# pos=int(input('enter the position: '))

# copy names from 0th position to pos-1
# temp_name=names[0: pos-1] #[start: stop]
# print (temp_name)

# temp_name=temp_name+new_nm
# print (temp_name)

# concatenate remaining elements of names from pos till end
# names=temp_name+names[pos: ]
# print (names)

# -------------------------------------------------------

# delete an elements from a particular position
num=(10,20,30,40,50,60,70,80)
print(num)
# accept position number from which element need to be deleted
pos=int(input(' enter position number: '))
# copy from 0th position to pos-1 into another tuple
num1=num[0:pos-1]
num=num1+num[pos:]
print(num)
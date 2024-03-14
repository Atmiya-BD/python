# 6 Accept student_name: age from the user. Perform following operations on it: 
# i). Give total of all students age
# ii). Find an average age of student
# iii). Student with highest age 
# iv). Give facility so as user can know the age of any student by inputting the students age.

dt={}

for i in range(1,5):
    key='student_name'+str(i)
    val=input('enter student name: ')
    dt.update({key:val})

    key='age'+str(i)
    val=int(input('enter student age: '))
    dt.update({key:val})        

print(dt)
print(dt.keys())

marks=[]
total=0
for i in range(1,5):
    key=('age'+str(i))
    total=total+int(dt[key])
    print(dt[key])
    marks.append(dt[key])
    
print("total is of age is: ", total)

average=total/4;
print("average is of age is: ", average)
print("highest age is: ",max(marks))

# find=int(input('enter age to find student name: '))
# print("name is: ", list(dt.keys()) [list(dt.values()).index(find)])

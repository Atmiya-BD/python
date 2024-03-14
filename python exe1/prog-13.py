#Write a program to swap two values without using third variable.


no1=float(input("enter first no: "))
no2=float(input("enter second no: "))

print("Before Swaping")
print("no1 is: {0} & no2 is: {1}".format(no1, no2))

no1=no1+no2
no2=no1-no2
no1=no1-no2

print("After Swaping")
print("no1 is: {0} & no2 is: {1}".format(no1, no2))

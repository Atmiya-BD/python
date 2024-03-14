#Write a program to read the value of X and Y and print the result of following expression (X+Y)/(X-Y)

x=float(input("enter value of X: "))
y=float(input("enter value of Y: "))

ans=(x+y)/(x-y)

print("Value of X is: {0} \nValue of Y is: {1} \n And result of (x+y)/(x-y) is : {2}".format(x, y, ans))

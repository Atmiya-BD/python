#Write a program to calculate area and perimeter of the rectangle.

length=float(input("enter length of the rectangle: "))
width=float(input("enter width of the rectangle: "))

area=length*width
perimeter=(length+width)*2

print("Length is: {0} \nWidth is: {1} \n Area is: {2} \n Perimeter is: {3}".format(length, width, area, perimeter))

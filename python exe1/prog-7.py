#The distance between two cities is input through keyboard. 
# Write a program to convert and print this distance in feet, meter, inch and centimeter.

dist_in_km=float(input("enter distance between two cities in km: "))

meter=dist_in_km*1000
centimeter=meter*100

feet=dist_in_km*3280.84
inch=feet*12
# 39370.1 =

print("Distance in km is : {0} \n it become in Meter: {1} \n it become in CM: {2} \n it become in Feet : {3} \n it become in Inch : {4} ".format(dist_in_km, meter, centimeter, feet, inch))

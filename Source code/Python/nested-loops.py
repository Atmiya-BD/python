#Nested loops
# Structure:
# 	Outer loop:
# 		Inner loop:

# for i in range(3):
# 	for j in range(4):
# 		print('i=',i,'j=',j)

# for i in range(4):
# 	print(i,end="")

# for i in range(3):
# 	for j in range(4):
# 		print(i,end="")
# 	print()

#Create square/rectangle by accepting rows, columns and symbol from user
# rows=int(input('Enter number of rows: '))
# columns=int(input('Enter number of columns: '))
# symbol=input('Enter number of symbol: ')
# for i in range(rows):
# 	for j in range(columns):
# 		print(symbol,end='')
# 	print()

#Left aligned, right angle triangle
# *
# **
# ***
# ****
# *****

for i in range(1,6):							
	for j in range(i):				
		print('*',end='')
	print()


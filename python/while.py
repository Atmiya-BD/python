#print 1 to 10 using while loop
'''
a=1
while a <= 10:
    print(a)
    a=a+1
print('End of while')
'''

#Allowing user to enter numbers, as soon as they insert 0, program will give sum of all the entered numbers

'''
total=0
number = int(input('Enter a number(Outside while loop):'))    #before while loop

while number != 0:
    total = total + number
    number = int(input('Enter a number(Inside while loop): '))
    #print('The number is: ',number)    //for displaying entered number
print('The sum of all the entered numbers is: ', total)
'''

#table

'''
num = int(input('Enter a number for which you want a table: ')) 
counter = 1

while counter <= 10:
    ans = num * counter
    print(num,'x',counter,'=',ans)
    counter = counter + 1
'''

#print even-odd numbers by taking user input


#Write a program to calculate simple interest.

p=int(input('Principle amount: '))
r=int(input('interest rate: '))
n=int(input('Number of years: '))

si=(p*r*n)/100;
total_amount=si+p

print("principle amount is :: {0} \n interest rate is :: {1} \n year is :: {2} \n interest is :: {3} \n total amount is : {4}".format(p,r,n,si,total_amount))
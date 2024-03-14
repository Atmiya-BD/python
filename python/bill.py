'''
discount (0,5000,>=
           5000 + 10, 
           8000 + 12, 
           10000 + 15, 
           20000 + 25)
'''

print('\n--------------- CALCULATE BILLING ---------------\n')

amount = int(input('Please enter a amount: '))

if amount <= 0:
    print('Opps!! Bill amount must be more than Zero.')

elif amount <= 5000:
    print('Purchase little more to avail discount')

elif amount >= 5000 and amount <=8000:
    print('You got 10% discount')
    print('Your Amount\t:',amount)
    discount = (amount*10)/100
    print('Your Discount\t:',discount)
    payable = amount - discount
    print('\n------------------------------')
    print('Payable amount\t:',payable)

elif amount >= 8000 and amount <= 10000:
    print('You got 12% discount')
    print('Your Amount\t:',amount)
    discount = (amount*12)/100
    print('Your Discount\t:',discount)
    payable = amount - discount
    print('\n------------------------------')
    print('Payable amount\t:',payable)

elif amount >= 10000 and amount <= 20000:
    print('You got 15% discount')
    print('Your Amount\t:',amount)
    discount = (amount*15)/100
    print('Your Discount\t:',discount)
    payable = amount - discount
    print('\n------------------------------')
    print('Payable amount\t:',payable)

elif amount >= 20000:
    print('You got 25% discount')
    print('Your Amount\t:',amount)
    discount = (amount*25)/100
    print('Your Discount\t:',discount)
    payable = amount - discount
    print('\n------------------------------')
    print('Payable amount\t:',payable)

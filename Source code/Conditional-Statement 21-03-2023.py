# if... elif... else

# when there is need of testing multiple condition and execute statements depending on those condition you can write several elif statements between if & else

# Syntax:
# if condition:
#     stetement1
# elif condition:
#     stetement2
# elif condition:
#     stetement2
# else:
#     stetement3

# when condition 1 is True, the statements 1 will be executed. 
# if condition 1 is false then condition 2 is eveluated.
# when condition 2 is True, the statements 2 will be executed.  when condition 2 is false, then condition 3 is tested, if condition 3 is True, then statements3 will be executed.when condition 3 is False, the statements 4 will be executed.
# it means statements 4(statements under else) will be executed only if none of the conditions are true

# program to know whether the given number is positive, negative or zero
# a=int(input('enter the number: '))
# if a>0:
#     print(a, 'is a positive number')
# elif a==0:
#     print('it is zero')
# else:
#     print(a, 'is a negative number')

#  a program to print the entered number into word
    # else is not menedadery while using if... and elif...

# a = int(input('enter the number: '))
# if a == 0:
#     print("zero")
# elif a == 1:
#     print("one")
# elif a == 2:
#     print("two")
# elif a == 3:
#     print("three")
# elif a == 4:
#     print("four")
# elif a == 5:
#     print("five")
# else:
#     print("the range is between 0 and 5")

# discount(0, 5000+10, 8000+12. 10000+15, 200000+25 )
# amount=int(input('please enter the amout: '))
# if amount<=0:
#     print('bill amount must be more than 0')
# elif amount<=5000:
#     print('purchase little more to avail discount')
# elif amount>=5000 and amount<=8000:
#     print('you got 10 percent discount')
# elif amount>=8000 and amount<=10000:
#     print('you got 12 percent discount')
# elif amount>=10000 and amount<=20000:
#     print('you got 15 percent discount')
# else:
#     print("hurry!, you got a maximum discount of 25 percent")

result
marks=int(input('enter your marks: '))
if marks<50:
    print('you need to re-appear in exam')
elif marks>=50 and marks<=60:
    print('you passed the exam')
elif marks>=60 and marks<=70:
    print('you passed the exam')
elif marks>=70 and marks<=80:
    print('you passed the exam')
elif marks>=80 and marks<=100:
    print('you passed the exam')
else:
    print('enter valid marks: ')

# discount(0, 5000+10, 8000+12. 10000+15, 200000+25 )
amount=int(input('please enter the amout: '))
if amount<=0:
    print('bill amount must be more than 0')
elif amount<=5000:
    print('purchase little more to avail discount')
elif amount>=5000 and amount<=8000:
    print('you got 10 percent discount')
    discount=(amount*10)/100
    print('amo
elif amount>=8000 and amount<=10000:
    print('you got 12 percent discount')
elif amount>=10000 and amount<=20000:
    print('you got 15 percent discount')
else:
    print("hurry!, you got a maximum discount of 25 percent")


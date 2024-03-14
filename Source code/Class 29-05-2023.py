# class employee:
#     def __init__(self, name, degree):
#         self.name = name
#         self.degree = degree
        
#     def printEmployee(self):
#         print('the name of employee is: ' + self.name)
#         print('the degree an employee hold is: ' + self.degree)

# e=employee('abc', 'bca')
# e.printEmployee()

# class department():
#     def __init__(self, experience,  name, degree):
#         super().__init__(name, degree)
#         self.dept= dept
#         self.experience = experience

#     def prentdept(self):
#         print('the department of employees is: ' + self.dept)
#         print('the experience of an employee is: ' + self.experience)

# d=department(10,'MCA)', 'phd')
# d.prentdept()
# d.printEmployee()

# types of inheritence

# the main advantage of inheritance is code reusability
# the members of he super/parent class are resuable in the sub/child classes
# there are mainly two types of inheritance
# single inheritance
# multiple inheritece

# single inheritance
# a single inheritance enables a derived class to inherit child class to inheritance properties of base/parent class thus enabling code resuablity and the addition of new features to existing code

# class father:
#     def func1(self):
#         print("father class: function")

# class child(father):
#     def func2(self):
#         super
#         print("child class: function")
# c=child()
# c.func1()
# c.func2()

# multiple inheritance
# deriving sub-classes from multiple base-classes is called multiple inheritance 
# in this type of inheritence, where will be more then one super/parent classes and there may be one or more sub/child classes 

# class father:
#     def func1(self):
#         print("father class: function")

# class mother:
#     def func2(self):
#         print("mother class: function")

# class son(father, mother):
#     def func3(self):
#         print("mother + father=child: function")

# s=son()
# s.func1()
# s.func2()
# s.func3()

# print(son.mro())
# method resulution order(mro)

# explain mro with example
#  in multiple inheritance sinarios, any specified attribute or method is searched first in the current class if not found, the search continues into parent class in depth-first, left-to-right fashion without searching the same class twice searching in this way is called method resulution order(mro)
# MRO folloes three principals seach for the sub class before going to its base class 
# when a class is inherited form several classes, it searches in the order from left to right and last it will not visit any class more then once

# class A:
#     def check(self):
#         print('in class A')

# class B:
#     def check(self):
#         print('in class B')

# # classes ordering
# class C(A,B):
#     def __init__(self):
#         print('constructor C')
# obj=C()
# print(C.mro()) # it prints the lookup order
#         # here, C is the name of the class

# Polymorphism
# the word "polymorphism" means having many forms
# in programming polymorphism means he same function name (but diffrent signatures) being use for different types

# the key difference is that the datatypes and number of arguments uses in the function to uderstand lets take an example of wheat flur
# using wheat flur we can make roti, breds, paratha
# the wheat flur is same but we can use it different forms.
# if a vairalbe, object, or method demonstrate different behavior in differnet context, is called polymorphism

# following topics are examples of polymorphism in python
# duck typing polymorphy
# operator overloading
# method overloading
# mothod overriding 

# the datatype of variables does not need to explicitly(manually) declare
# the type is implicitly(automatically) depending upon the purpose for which the variable is used

# a='atmiya'
# print(a)
# print(type(a))

# a=7
# print(a)
# print(type(a))

# class Duck:
#     def speak(self):
#         print("quack quack ")

# class Human:
#     def speak(self):
#         print("namaste ")

# def call_speck(obj): #this method accepts an object and calls speck method
#     obj.speak()
# # calling the call_speak() method and pass and object
# # depending upon the type of object, talk() method is executed
# a=Duck()
# call_speck(a)

# a=Human()
# call_speck(a)

# operator overloading
# an operators like +, -, *, /,etc is a symbol that perform some actions as we know that '+' is an operator perform addition when used on numbers
# when '+' is used on strings then strings are concatenated 
# when an operator performs different actions it is said to be operator overloading

# operator overloaing
# a=10
# b=6

# print(a+b) #using '+' to add two numbers

# str1='atmiya'
# str2='uni'
# print(str1+str2) #using '+' to concatenate two strings

# lst1=[1,2,3]
# lst2=[11,22,33]
# print(lst1+lst2)

# program to overload greater than(>) operator
# class ramayan:
#     def __init__(self,no_of_sloks):
#         self.no_of_sloks = no_of_sloks

#     def __gt__(self,other):
#         return self.no_of_sloks>other.no_of_sloks

# class mahabhart:
#     def __init__(self,no_of_sloks):
#         self.no_of_slocks=no_of_sloks
# r=ramayan(24000)
# m=mahabhart(4000)

# if r>m:
#     print('ramayan has more slocks')
# else:
#     print('mahabharat has more slocks')

# method overloading
# if a method is written such that it can perform more then one task, it is called method overloading. 
# method overloading is not available in python
# in python we can archieve method overloading by writing same method with saveral parameters.
# the method performs the operation depending on the number of arguments in the method call

# class add:
#     def sum(self,a=None, b=None, c=None):
#         if a!=None and b!=None and c!=None:
#             print('the addition of 3 numbers is: ',a+b+c)
#         elif a!=None and b!=None:
#             print('the addition of 2 numbers is: ',a+b)
#         else:
#             print('enter atleast 2 numbers')

# a=add()
# a.sum(10)
# a.sum(10,20)
# a.sum(10,20,30)

# method overridding
# when there is method is the parent class, writing the method in the child class so that it replaces the parent class method is called method overriding

# the programmer overrides the parent/super class method when he doen not want to use them in sub/child class

# instead he wants an new functionality to the same method in the sub class

# program to find area of square and circle
import math
class square:
    def area(self, a):
        print('the area of square is: ',a*a)

class circle(square):
    def area(self, a):
        print('the area of circle is: ',math.pi*a*a)
# pi=3.14

c=circle()
c.area(10)

s=square()
s.area(15)

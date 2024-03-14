#Write a program to find out the net salary of an employee and get the basic salary from him. 
# Applicable TA 4%, DA 30%, HRA 15% on basic salary. 
# Applicable 3% tax 12% PF on basic salary.

basic_salary=float(input("enter your salary: "))

net_salary=basic_salary

print("Basic Salary is: ",basic_salary)

# TA -> 4%
net_salary+=(basic_salary*4)/100
print("Net salary after Adding 4% TA: ", net_salary)

# DA -> 30%
net_salary+=(basic_salary*30)/100
print("Net salary after Adding 30% DA: ", net_salary)

# tax -> 3%
net_salary-=(basic_salary*3)/100
print("Net salary after Diducting 3% TAX: ", net_salary)

# PF -> 12%
net_salary-=(basic_salary*12)/100
print("Net salary after Adding 12% PF: ", net_salary)

# 8 Take following values from the user: Name (It must allow only alphabet in capital letters), 
# Age (Only number), 
# Address (Must be alpha numeric). 
# If all the constraints are fulfilled than display all values

# prompt user to enter name, age, and address
name = input("Enter your name (must be all capital letters): ")
age = input("Enter your age (must be a number): ")
address = input("Enter your address (must be alphanumeric): ")

# check constraints and display values if all constraints are fulfilled
if name.isalpha() and name.isupper() and age.isnumeric() and address.isalnum():
    print("Name:", name)
    print("Age:", age)
    print("Address:", address)
else:
    print("Constraints not fulfilled.")


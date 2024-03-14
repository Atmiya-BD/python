# 4 Accept value of tuple from the user. Apply all functions to process tuple

print("enter some values seperated by space only: ")
tpl=input("").split(" ")
print(tpl)

# find length of tuple
print(len(tpl))

# append values in
tpl.append("orange")
print(tpl)

# remove elements from tuple
tpl.remove('A')
print(tpl)

# delete all elements from tuple
# del tpl
print(tpl)

# Add tuple to a tuple
tpl = ("apple", "banana", "cherry")
y = ("orange",)
tpl += y

print(tpl)
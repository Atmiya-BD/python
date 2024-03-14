# 5 Accept values from the user in the form of key:value, apply all dictionary methods.

dt={"brand": "Ford",
  "model": "Mustang",
  "year": 1964}
print(dt)

# clear dictionary
dt.clear()
print(dt)

element=int(input("enter how many record you want to insert: "))
for a in range(element):
    print('enter key: ')
    key=input()
    print('enter value: ')
    val=input()
    dt.update({key:val})
print(dt)

# copy dictionary 
new_dt=dt.copy()
print(new_dt)

# create a new dictionary with values 0
dt=dt.fromkeys(dt, 0)
print(dt)

# dt=dt.get("model")
# dt=dt.get("price", 15000)
print(dt)

#  update dictionary
dt.update({"color": "White"})
print(dt)

print(dt.items())
print(dt.keys())
print(dt.values())

dt.setdefault("color", "white")
print(dt)

dt.popitem()
# dt.pop("brand")
print(dt)
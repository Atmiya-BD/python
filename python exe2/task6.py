# 6). Create a set containing varieties of value and perform following task:
myset={10.23, 3, 23, 24, 25, 26, 25, 25, True, "abc", "rajkot", "atmiya"}
print(myset)

# -Try to insert the duplicate value.
# myset.add(23.3)
myset.add(23)
print(myset)

# -Add two values in the set.
myset.update("rk", "jk")
# myset.update("rk", 111)
# myset.update(222, 111)
print(myset)

# -Remove two values from the set.
myset.remove('abc')
# myset.remove('3')
myset.remove(3)
print(myset)
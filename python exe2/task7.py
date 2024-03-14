# 7). Create a set containing varieties of value and perform following task (the set must be not modifiable):
myset={10.23, 3, 23, 24, 25, 26, 25, 25, True, "abc", "rajkot", "atmiya"}
myset=frozenset(myset)
print(myset)

# -Try to insert the duplicate value.
# myset.update(23)
# print(myset)
# Note: frozenset is not changeable

# -Add two values in the set.
# myset.update(222, 111)
# print(myset)
# Note: frozenset is not changeable

# -Remove two values from the set.
myset.remove(3)
print(myset)
# Note: frozenset is not changeable

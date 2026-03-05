"""
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
"""
x = ["Spoon", "Fork", "Plate"]
y = ["Spoon", "Fork", "Plate"]
z = y
print(y is z)
# Answer is true bcuz theyre sharing the same memory location
print(x is y)
# Answer is false bcuz x is not the same object as y or bcuz theyre not sharing the same memory location
print(x == y)
# Equal to ( == ) counts how many items in a list
# is not
print(x is not y)
print(z is not y)
print(x != z )
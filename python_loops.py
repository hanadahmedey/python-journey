"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""
"""items = ["Phone", "Keys", "Pen", "Watch"]
for x in items:
    print(x)

for letter in "Hanad":
    print(letter)"""
for name in "python":
    if name == "h":
        continue
    print(name)
for word in "codin":
    pass
# Nested loops
#A nested loop is a loop inside a loop
#The "inner loop" will be executed one time for each iteration of the "outer loop"
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
items = ["Phone", "Keys", "Pen"]
for x in adj:
    for y in fruits:
        for z in items:
            print(x, y,z)




"""
List[]
Tuple()
Set{}
"""
#Python list
_balls = ["Football","Basketball","Volleyball","Baseball","Tennis ball","Soccer ball","Bowling ball","Rugby ball"]
print(_balls[0])
#slice
print(_balls[0:6])
print(_balls[0:8])
"""
Lists are used to store multiple items in a single variable
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
Lists are created using square brackets
"""
#list length
print("The list has", len(_balls), "items")
print(type(_balls))
#negative indexing
print(_balls[-1])
print(_balls[-4:])
print(_balls[-4:])
print(_balls[:4])

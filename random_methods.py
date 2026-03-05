import random
# Shuffle a list (reorganize the order of the list items)
items = ["Bottle", "Watch", "Lamp", "Jacket", "Mug", "Towel"]
random.shuffle(items)
print(items)
# Choice returns a random element from a list
print(random.choice(items))
# Sample returns a list that contains any 2 of the items from a list
print(random.sample(items, k=3))

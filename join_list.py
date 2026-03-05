_balls = ["Football","Basketball","Volleyball","baseball","Tennis ball","Soccer ball","Bowling ball","Rugby ball"]
itemlist = ["Notebook", "Pen", "Water bottle", "Phone charger", "Backpack", "Headphones", "Wallet", "Keys", "Sunglasses", "Snack bar"]
print(_balls + itemlist)
_balls.extend(itemlist)
print(_balls)
for x in itemlist:
    _balls.append(x)
    print(_balls)
#adding items to a list
itemlist.append("Pencil")
print(itemlist)
_balls.clear()
print(_balls)
itemlist.insert(0,"book")
print(itemlist)
itemlist.pop(0)
#The pop() method removes the element at the specified position
print(itemlist)
itemlist.remove("Keys")
print(itemlist)

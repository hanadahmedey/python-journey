with open("python word.txt", "a") as x:
    x.write(input("enter your text here"))

with open("python word.txt") as y:
    print(y.read())
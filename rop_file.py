x = open("python word.txt")
print(x.readline())
print(x.readline())
with open("python word.txt") as x:
  for y in x:
    print(y)
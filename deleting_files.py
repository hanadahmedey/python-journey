"""import os
x = os.listdir("hanad_python_coding")
print(x)
import os
print(os.getcwd())
import os
print(os.path.exists("hanad_python_coding")
      """
import os

folder = "C:\Users\Kenya\Desktop\hanad_python_coding"

if os.path.exists(folder):
    for file in os.listdir(folder):
        print(file)
else:
    print("Folder not found!")

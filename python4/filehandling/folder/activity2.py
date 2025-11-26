new_file = open('new_file.txt', 'x')
new_file.close()

import os
print("checking my file to see if it exists or not ....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")

my_file = open("my file.txt", "w")
my_file.write("Hi my name is penguin")
my_file.close()

os.remove('read.txt')

os.rmdir('folder')
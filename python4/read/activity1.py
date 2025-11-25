file = open('read.txt','r')
print(file.read())
file.close()


file = open('read.txt','r')
print("\n read in parts \n")
print(file.read(8))
file.close()

file = open('read.txt', 'a')
file.write("Hi I am Penguin and i am 1 yr old")
file.close()
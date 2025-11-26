with open('read.txt', 'w') as file:
    file.write("Hi! I am penguin")
file.close()

with open('read.txt', 'r') as file:
    data = file.readlines()
    print("words in this file are ....")
    for line in data:
        word = line.split()
        print (word)

file.close()
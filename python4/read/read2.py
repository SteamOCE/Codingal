file_read = open('read.txt', 'r')
print("File in read mode -")
print(file_read.read())
file_read.close()

file_write = open('read.txt', 'w')
file_write.write("file in write mode .... ")
file_write.write("Hi my name is Penguin")
file_write.close()

file_append = open('read.txt', 'a')
file_append.write("\n file in apend mode ...." )
file_append.write("I am Penguin")
file_append.close()


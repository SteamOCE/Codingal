file1 = open('read.txt', 'r')

file2 = open('readupdated.txt', 'w')

for line in file1.readlines():

         if not (line.startswith('coding')):

                print(line)
                file2.write(line)

file2.close()
file1.close()

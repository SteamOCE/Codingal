firstfile = "Codingal.txt"
secondfile = "sample_doc.txt"

f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')

print('content of first file before appending -\n', f1.read())
print('content of second file before appending -\n', f2.read())

f1.close
f2.close

f1 = open(firstfile, 'a+')
f2 = open(secondfile, 'r')

f1.write(f2.read())

f1.seek(0)
f2.seak(0)

f1.close()
f2.close()

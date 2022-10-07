fileobj = open ("F:/python/test.txt")
fileobj = open ("F:/python/test.txt",'r')
#fileobj = open ("F:/python/test.txt",'w')
#fileobj = open ("F:/python/test.txt",'a')
"""
print(fileobj.read())
fileobj.seek(0)
print(fileobj.read())
fileobj.seek(10)
print(fileobj.read())
print(fileobj.read(50))
fileobj.seek(0)
print(fileobj.readline())
fileobj.seek(0)
print(fileobj.readlines())
fileobj.seek(0)
"""
"""
# to print first 5 lines 
count = 0
for i in fileobj.readlines():
    if (count<5):
        print(i)
    else:
        break
    count += 1

fileobj1 = open ("F:/python/test1.txt",'w')
fileobj1.write("i am appending to the old file")
fileobj1.close()
fileobj1 = open ("F:/python/test1.txt",'r')
print(fileobj1.read())
fileobj1.close()
fileobj1 = open ("F:/python/test1.txt",'a')
fileobj1.write("i am appending to the old file")
fileobj1.close()
fileobj1 = open ("F:/python/test1.txt",'r')
print(fileobj1.read())
fileobj1.close()

import os
os.remove("F:/python/test1.txt")
fileobj1 = open ("F:/python/test1.txt",'r')
"""
with open ("F:/python/test1.txt") as file:
    data = file.read()
with open ("F:/python/test1.txt",'w') as file:
    file.write("hello world")

with open ("F:/python/test1.txt",'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
    








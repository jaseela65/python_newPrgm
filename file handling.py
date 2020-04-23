'''f=open("file1.txt", "r")
print(f.read())

print(f.readline())
print(f.readline())


for x in f:
   print(x)

   
f1=open("file1.txt", "a")#append file
f1.write("Now the file has more content!")
f1=open("file1.txt", "r")
print(f1.read())

f2=open("file1.txt", "w")
f2.write("Now the file has more content!")
f2=open("file1.txt", "r")
print(f2.read())'''

import os
print(os.path.exists("file1.txt"))


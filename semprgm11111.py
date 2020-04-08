'''# while loops
n = 5
while n > 0:
    n -= 1
    print(n)


#..........................

i = 1
while i < 6:
  print(i)
  i += 1


#...................
#  while... else

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#.........................................

# break and continue stmts...

n = 5 
while n > 0:
    n -= 1 
    if n == 2: 
      break  
    print(n)  
print('Loop ended.')


n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')

#................................

# infinite loops

while True:
   print('hello')



num = 1
while num<5:
   print(num)
   break


#.............................
# Nested while loops

i = 1
j = 5
while i < 4:
    while j < 8:
        print(i, ",", j)
        j = j + 1
        i = i + 1


#...........................
# one line  while loops

n = 5
while n > 0:  n -= 1; print(n) 

#................................
a=3
if a<10:
   print("a is less than 10")
   while a<5:
     print("a is less than 5")
     break
      
else:
     while a>10:
          print(" a is greater than 10")
          break
print("main prgrm")          

#........................................
x=int(input())
while x<25:
     if x<=20:
          print("x is between 0 and 20")
     elif x<=10:
          print("x is between 0 and 10")
     else:
          print("x is between 20and 25")
     break
print("prgrm terminated")          
          
          




          







     



         













    




















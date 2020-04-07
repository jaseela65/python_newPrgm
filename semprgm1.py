# while loops
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
'''
while True:
     print('foo')
'''


a = ['foo', 'bar', 'baz']
while True:
    if not a:
        break
    print(a.pop(-1))


#.............................
# Nested while loops

a = ['red', 'black']
while len(a):
     print(a.pop(0))
     b = ['orange', 'apple']
     while len(b):
         print('>', b.pop(0))


#...........................
# one line  while loops

n = 5
while n > 0:  n -= 1; print(n) 





         













    




















# print number from 1 to 6
a=0
while a<=6:
    print(a)
    a+=1
# print only even numbers given from user input

a=int(input())
if a%2==0:
    print("even")
else:
    print("not even")

#print only even numbers from 0 to 20

a=0
while a<=20:
    a+=2
    print(a)
    
    
# print multiplication table of 5
a=1
b=5
while a<=10:
    c=a*b
    print(a," * ",b,"=",c)
    a+=1

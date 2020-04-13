
# program 1
# check a number is prime or not

a=int(input("enter a number"))

for i in range(2,a-1):
    if a% i==0 :
       print("not prime")
       break
else:
   print("prime no")

#.....................................................................
   

# program 2

#check list of prime numbers within a range
a=int(input())
b=int(input())
d=[]
for i in range(a,b):
      for j in range(2,i-1):
         if i% j==0 :
             #print("not prime")
             break
         continue
        
      else:
          d.append(i)
          
else:
    
    print("prime no",d)

#...................................................................


# program 3

# check a number is armstrong or not

num = int(input("Enter a number: "))
sum1 = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum1=sum1+ digit ** 3
   temp =temp// 10

if num == sum1:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#..................................................................

#program 4
    
#sum of digits
a=input()
b=len(a)
sum=0
for i in range(0,b):
    sum=sum+int(str(a)[i])

else:
    print(sum)

#.................................................................


#program 5
    
# product of digits

a=input()
b=len(a)
sum=1
for i in range(0,b):
    sum=sum*int(str(a)[i])

else:
    print(sum)


#.................................................................

#program 6   
# add all odd numbers,even numbers seperately and checks both sum are equal
 

a=[1,2,3,4,1,1]

print(a)
even=[]
odd=[]
sum1=0
sum2=0
for i in a:

       if i%2==0:
          even.append(i)
          sum1=sum1+(i)

       else:
          odd.append(i)
          sum2=sum2+int(i)
    
else:
    print(sum1)
    print(sum2)

    
    if sum1==sum2:
       print("True")
    else:
        print("False")

#.....................................................................        


#program  7
# add all the positive and negative no and check sum of both are equal

a=[2,3,-4,5,-6]

print(a)
pos=[]
neg=[]
sum1=0
sum2=0
for i in a:
       if i>0:
          pos.append(i)
          sum1=sum1+(i)

       else:
          neg.append(i)
          sum2=sum2+(i)
    
else:
    print(sum1)
    sum2=sum2*-1
    print(sum2)

    if sum1==sum2:
       print("sum is equal")
    else:
        print("sum is not equal")


   

#...........................................................

# program 8

# print fibonaacci series
a=int(input())
print("\n")
f=0
s=1
t=0
print(f)
print(s)
for i in range(0,a):
    
    t=f+s
    print(t)
    f=s
    s=t
    

#.............................................................

#program 9
    
# factorial of a number
a=int(input())
fact=1
for i in range(1,a+1):
    fact=fact*i
    

else:
    print("factorial of  ",a," :",fact)

#.............................................................

#program 10
    
#get a list/ set of numbers from user

a=list()
len=int(input())

for i in range(len):
    n=int(input())
    a.append(n)
else:
    print(a)

#.............................................................


#program 11
    
#get a list/set of strings from user

a=list()
len=int(input())

for i in range(len):
    n=input()
    a.append(n)
else:
    print(a)


#................................................................

#program  12
# get a dictionary from user

d=dict()
len=int(input())

for i  in range( len):
        j=input()
        d.update({i:j})
    
else:
    print(d)

#................................................................

#program   13
    
#check wheather a vowel is present in a string or notand find the number of occurences

a=input()
i=a.count('i')+a.count('a')+a.count('e')+a.count('o')+a.count('u')
if i!=0:
    print(" string contain vowels",i,"times occured")
else:
    print("string not contain vowels")

#............................................................

#program 14
# fizzbuzz
# 2 15
#  %3--fizz
# %5--buzz
# %3 and %5--fizzbuzz

a="fizzbuzz"
b=int(input())
c=int(input())
for i in range(b,c+1):
    if i%3==0 and i%5==0:
        print(a)
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print("na")
    


    





















    
    




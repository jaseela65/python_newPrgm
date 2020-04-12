# check a number is prime or not

a=int(input("enter a number"))

for i in range(2,a-1):
    if a% i==0 :
       print("not prime")
       break
else:
   print("prime no")

#check list of prime numbers within a range
a=int(input())
b=int(input())
d=[]
j=2
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
   
# check a number is armstrong or not

a=input("enter a number")
b=int(a[0])**3+int(a[1])**3+int(a[2])**3
print(b)
a=int(a)
if a==b:
    print("armstrong no")
else:
    print("not armstrong")




    


    
    









    
    




'''#check  wheather a string is palindrome or not
a=input()
b=a[ : :-1]
if a==b:
    print("given string is palindrome")
else:
    print("given string is not palindrome")

#get a mark from student()
#0-100 valid
#100 grade a
#90 to99  grd b
#80 89 grd c
#70 to 79 grd d
#50 to 69 grade e
#0 to 49 fail grade f
#other wise invalid

a=int(input())
if 0< a < 100 :
  print("valid")
if a==100:
    print("grade : A")
elif 90<=a<=99 :
    print(" grade :B")
elif 80<=a<=89:
    print(" grade :C")
elif 70<=a<=79:
    print(" grade :D")
elif 50<=a<=69:
    print(" grade :E")
elif 0<=a<=49:
    print(" grade :F")
else:
    print(" invalid")


# prgrm 3
# check wheather first char, middle char,last char of a string is same or different

a=input()
b=int(len(a)//2)
if a[0]==a[b]==a[-1]:
    print("True")
else:
    print("False")


#prgrm 4
# get two numbers from user
#23
#5
# true if  sum of first number is equal to second number(2+3=5)
#otherwise false

a=int(input("enter first number : "))
b=int(input("enter second number : "))
val1=int(str(a)[0])
val2=int(str(a)[1])
c=val1+val2
if c==b:
   print("true")
else:
   print("false")



    # check wheather a vowel is present in a string and  print no of occurences
    
'''
an=list(input())
c=0
if  'a' in an or 'e' in an or 'i' in an or 'o' in an or 'u'in an:
    print("vowel is find in given string")
    d=an.count('a')+an.count('e')+an.count('i')+an.count('o')+an.count('u')
    print(d," times occured")
else:
    print( " no vowels are found")


    
    
    












   


    



















    
    
    




















    





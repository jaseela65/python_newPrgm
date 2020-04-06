 # python syntax

a="Hello World! "
print(a) # Hello World! 

 # variable

x="python is "
y="language"
print(x+y) # python is language

 # python numbers

a=10
print(type(a))#<class 'int'>

b=2.5
print(type(b))#<class 'float'>


a=3j
b=4+5j
print(type(a))#<class 'complex'>
print(type(b))#<class 'complex'>

 # python casting

a=int(1)
b=int(3.9)
c=int("3")
print(a) # 1
print(b) #3
print(c) #3

a= float(3)
b=float(9.5)
c=float("5")
print(a) #  3.0
print(b) # 9.5
print(c) #5.0

x = str("s1")  
y = str(2)    
z = str(3.0)  
print(x) #  's1'
print(y) #  '2'
print(z) # '3.0'

 # python strings

a=" language "
print(a[1]) #l
print(a[2:5]) #ang
print(a.strip()) # language
print(len(a)) #10
print(a.lower()) #language
print(a.upper()) # LANGUAGE
print(a.replace("l","s")) #sanguage
a="Hello World!"
print(a.split()) # ['Hello', 'World!']


   # Python Operators

a=10
b=5
print("addition:",a+b) # addition: 15
print("subtraction:",a-b)  # subtraction: 5
print("Multiplication",a*b) #Multiplication 50
print("division:",a/b) #division: 2.0
print("Modulo division :",a//b) #Modulo division : 2
c=a
print("assignment :",c) # assignment : 10


    # Python List

a=[2,4,5,6,9,7,8]

print(type(a)) # <class 'list'>
print(a[1]) #  4

a[3]=55
print(a) # [2, 4, 5, 55, 9, 7, 8]
print(len(a)) #7

a.append(404) 
a.insert(2,'hi')
print(a) #[2, 4, 'hi', 5, 55, 9, 7, 8, 404]

a.remove(5) #[2, 4, 'hi', 55, 9, 7, 8, 404]
print(a)  

a.pop() 
print(a)#[2, 4, 'hi', 55, 9, 7, 8]

del a[5]
print(a) # [2, 4, 'hi', 55, 9, 8]

a.clear()
print(a) #[]

a=list([66,8,90])
print(a) [66, 8, 90]


     # python Tuple


a=(2,45,"rt",98)
print(a[2]) #rt
print(len(a)) # 4
del a
a=tuple((2,'l','kk',90))
print(a) #(2, 'l', 'kk', 90)

      # python set

a={2,3,'ty',98,55,44,23}
print(a) #{2, 3, 98, 44, 23, 55, 'ty'}
a.add(354) 
print(a) # {2, 3, 'ty', 98, 354, 44, 23, 55}
a.update('rr','gh','ert')
print(a) # {2, 3, 98, 354, 'h', 'e', 't', 44, 23, 'ty', 55, 'g', 'r'}
print(len(a))
a.remove(44)
print(a)#{'h', 'e', 2, 3, 98, 354, 'g', 'ty', 23, 55, 'r', 't'}
a.discard(354)
print(a)# {'h', 'e', 2, 3, 98, 'g', 'ty', 23, 55, 'r', 't'}
a.pop()
print(a)
a.clear()
del a
a=set({98,55,44,23})
print(a)  # {98, 44, 23, 55}

      # python Dictionary


a={1:23333332,2:'ell',3:'hi',4:'rty',5:789}
b=a[1]
print(b)

a[1]=233
print(a)

print(a.keys()) #dict_keys([1, 2, 3, 4, 5])
print(a.values()) #dict_values([233, 'ell', 'hi', 'rty', 789]) 

print(len(a))# 5
a[7]="red"
print(a) # {1: 233, 2: 'ell', 3: 'hi', 4: 'rty', 5: 789, 7: 'red'}

del a[3]
print(a) # {1: 233, 2: 'ell', 4: 'rty', 5: 789, 7: 'red'}

a.clear()
print(a) #{}

a=dict({1:'rt',2:67})
print(a) #{1: 'rt', 2: 67}


































































   























































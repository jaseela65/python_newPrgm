#Library Management From User and Admin ends
#books details
books={
    "python_Crash_Course":3,
    "programming_with_Java":3,
    "Object oriented programming with c++":2,
       }
print("----------LIBRARY MANAGEMENT FROM USER ADMIN ENDS-----------")
print("------------------------------------------------------------")

import datetime
d=datetime.date(2020,4,24)
i=0
while i<6:
    a=input("\nEnter u are admin or user:\n ")
    if a=="admin":
        print("\n.....Enter any of the choices given below.....\n")
        print(".....Enter number1 for viewing all books names...")
        print(".....Enter number2  for adding some new books .....\n")
    elif a=="user":
        print("\n.....Enter any of the choices given below.....\n")
        print(".....Enter number3 for viewing all book names...")
        print(".....Enter number4  for issuing a books .....")
        print("....Enter number 5 for return the book and check  for any penalty.....")
    else:
        print("wrong login")
    ds=list()
    ch=int(input("Enter any number :"))
    if ch==1 and a=="admin" :
        print("\n")
        for x in books:
            print(x)
    elif ch==2 and  a=="admin":
        a1=input("\nEnter the new book name:")
        a2=int(input("Enter the number of availablebooks:"))
        a11=dict()
        a11[a1]={a2}
        books.update(a11)
        print("\n")
        for x in books:
            print(x)
    elif ch==3 and a=="user":
        print("\n")
        for x in books:
            print(x)
        
    elif ch==4 and a=="user":
        b11=dict()
        print("\n")
        for x in books:
            print(x)
        b1=input("\nEnter the book name you want  :")
        if b1 in books:
            print("yes, this book is available")
            books.pop(b1)
            print("\n")
            for x in books:
                print(x)
        else:
            print("wrong entry ...this book is not available")
    elif ch==5 and a=="user":
        c1=input("\nEnter the new book name  u returned:")
        c2=input("Enter the author of that book:")
        c11=dict()
        c11={c1:c2}
        books.update(c11)
        print("\n")
        for x in books:
            print(x)
        today=datetime.date.today()
        d1=int(d.strftime("%d"))
        t1=int(today.strftime("%d"))
        c=int(t1-d1)
        ct=0
        if c>0:
            ct=c*20
            print("u are",c,"days late so u will pay..",ct)
        else:
            print("congratz u return the book at coorect time")
        
    
    else: 
         print("......Wrong Entry......")
         print(".......please try again.....")
         i=i+1
         continue
    i=i+1

else:
    print("........Run The Program Again....")



          

         
        
         
         

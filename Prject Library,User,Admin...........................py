##Library Management From User and Admin ends
#books details
books={
    "python_Crash_Course":1,
    "programming_with_Java":3,
    "Object oriented programming with c++":2,
       }
print("------------------------------------------------------------")
print("----------LIBRARY MANAGEMENT FROM USER ADMIN ENDS-----------")
print("------------------------------------------------------------")

import datetime
d=datetime.date(2020,4,24)
i=0
bk=books.copy()
while i<6:
    a=input("\nEnter u are admin or user:\n ")
    if a=="admin":
        print("\n.....Enter any of the choices given below.....\n")
        print(".....Enter number1 for viewing all books names...")
        print(".....Enter number2  for adding some new books .....")
        print(".....Enter number6  for viewing issued books by user .....\n")
    elif a=="user":
        print("\n.....Enter any of the choices given below.....\n")
        print(".....Enter number3 for viewing all book names...")
        print(".....Enter number4  for issuing a books .....")
        print("....Enter number 5 for return the book and check  for any penalty.....")
    else:
            print("wrong login")
    
    issued_book=dict()
    issued_book=books
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
        bk.update(a11)
        issued_book.update(a11)
        print("\n")
        for x in books:
            print(x)
    elif ch==3 and a=="user":
        print("\n")
        for x in books:
            print(x)
        
    elif ch==4 and a=="user":
        print("\n")
        for x in issued_book.items():
            print(x)
        b1=input("\nEnter the book name you want  :")
        if b1 in issued_book and issued_book[b1]==0:
            print("This book is not available")
            continue     
        else:
            print("yes, this book is available")
            count=issued_book[b1]-1
        issued_book.update({b1:count})
        print("Books available in the library is given below...\n")
        for x in issued_book.items():
            print(x)
        
    elif ch==5 and a=="user":
        c1=input("\nEnter the  book name  u returned:")
        if c1 in issued_book:
            count=issued_book[b1]+1
        issued_book.update({c1:count})
        print("Books available in the library is given below...\ ")
        for x in issued_book.items():
            print(x)
        today=datetime.date.today()
        d1=int(d.strftime("%d"))
        t1=int(today.strftime("%d"))
        c=int(t1-d1)
        ct=0
        if c>1:
            ct=c*20
            print("u are",c,"days late so u will pay..",ct)
        else:
            print("congratz u return the book at coorect time")
    elif ch==6 and a=="admin":
        print("\nIssued books are\n")
        diff=dict()
        diff=set(bk.items())-set(issued_book.items())
        print(diff)
    else: 
         print("......Wrong Entry......")
         print(".......please try again.....")
         i=i+1
         continue
    i=i+1

else:
    print("........Run The Program Again....")

        
        
        
        
        
        
    
    
    
          
    
      
    
   
    

            

    

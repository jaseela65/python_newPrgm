#Library Management From User and Admin ends

#admmin add book
books={
    "python_Crash_Course":{
        "Python Crash Course 2nd Edition written by Eric Matthes":2
        },
    "programming_with_Java":{
        "Programming with Java 4th edition written by  E. Balagurusamy":2
        },
    "Object oriented programming with c++":{"Programming with cpp 4th edition written by E. Balagurusamy":2}

        
   }
#admin add user
user={"a1001":"John","a1002":"Tom","a1003":"Deepa"}
print(".....if u are admin then enter any of the choices given below.....\n")
print(".....Enter number1 for viewing all books names...")
print(".....Enter number2  for adding some books .....")
print(".....Enter number3 for view issued books......\n")
print(".....if u are user then enter any of the choices given below.....\n")
print(".....Enter number1 for viewing all book names...")
print(".....Enter number2  for viewing books names.....")
print("....Enter number 3 for viewing current book details.....")
import datetime
d=datetime.date(2020,4,24)

i=0
while i<2:
    a=input("Enter u are admin or user:\n ")
    ds=list()
    ch=int(input("Enter any number :"))
    if ch==1 and a=="admin" :
        for x in books:
            print(x)
    elif ch==2 and  a=="admin":
        a1=input("Enter the new book name:")
        a2=input("Enter book details:")
        a11=dict()
        a11[a1]={a2}
        books.update(a11)
        for x in books:
            print(x)
    elif ch==3 and a=="user":
        b11=dict()
        for x in books:
            print(x)
        b1=input("Enter the book name:")
        if b1 in books:
            print("yes, this book is available")
            books.pop(b1)
            for x in books:
                print(x)
        else:
            print("wrong entry ...this book is not available")
    elif ch==4 and a=="user":
        c1=input("Enter the new book name  u returned:")
        c2=input("Enter the author of that book:")
        c11=dict()
        c11={c1:c2}
        books.update(c11)
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
        
        
        
        
        
        
    
    
    
          
    
      
    
   
    

            

    

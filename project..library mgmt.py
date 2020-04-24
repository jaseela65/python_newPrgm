#Library Management From User and Admin ends

#admmin add books
books={
    "python_Crash_Course":{"Author": "Eric Matthes",
     "Description":"Python Crash Course, 2nd Edition",
     "count": 2
                          },
    "programming_with_Java":{"Author":"E. Balagurusamy",
    "Description":"Programming with Java 4th edition",
    "count":1
    },
    "Object oriented programming with c++":{"Author":"E. Balagurusamy",
    "Description":"Programming with cpp 4th edition",
    "count":3
        }
   }
#admin add user
user={"a1001":"John","a1002":"Tom","a1003":"Deepa"}
a=input("Enter u are admin or user:\n ")
b="admin001"
c="user"
if c==a:
    p=input("enter user id:")
    x=user.get(p)
    print("Hello",x)
    print(".....Enter number1 for viewing all books names...\n")
    print(".....Enter number2  for isssuing  a book .....\n")
    print(".....Enter number3 for return a book......\n")
    choice1=int(input("Enter any number:"))
    if choice1==1:
        print(books.keys())
        q=input(".....Enter  any book name available in this library\nfor printing its specific details:\n" )
        print(books.get(q))
    elif choice1==2:
        r=input("enter the book u are selected:")
        if books[r]["count"]==0:
            print("book is not available")
        else:
            books[r]["count"]=books[r]["count"]-1
        print(books[r])
    elif choice1==3:
        s=input("which Book is u return:")
        books[s]["count"]=books[s]["count"]+1
        print(books[s])
    
        
elif b==a:
    print(".....Enter number1 for viewing users...\n")
    print(".....Enter number2  for viewing books names.....\n")
    print("....Enter number 3 for viewing current book details")
    

    choice=int(input("Enter any number:"))
    if choice==1:
        print(user.items())
    elif choice==2:
        print(books.keys())
    elif choice==3:
        t=input("Enter Book name:")
        print(books.get(t))
        
    






    

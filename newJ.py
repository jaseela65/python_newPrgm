##Library Management From User and Admin ends
#books details
books={
    "python_Crash_Course 2nd edition by Eric Matthes":5,
    "Beginning Django book by Daniel Rubio":5,
    "Python Trics book by DanBader":5,
    "Head First Python 2nd edition by by Paul Barry":5,
    "Learn Python the Hard Way 3rd edition by Zed":5,
    "Python Programming 3rd edition by John Zelly":5,
    "A Byte of Python by C.H Swaroop":5,
    "Django for Proffessionals books by William.S.Vincent":5,
    "programming_with_Java written by E.Balagurusamy":5,
    "Object oriented programming with c++ 4th edition Lafore ":5
    
       }
print("------------------------------------------------------------")
print("----------LIBRARY MANAGEMENT FROM USER ADMIN ENDS-----------")
print("------------------------------------------------------------")

import datetime
d=datetime.date(2020,4,24)
i=0
updated_books=books.copy()#updated books are just copy of books used for comparing with issued books
while i<4:
    a=input("\nEnter u are admin or user:\n ")
    if a=="user":
        print("\n.....Enter any of the choices given below....\n")
        print(".....Enter number1 for viewing all book names...")
        print(".....Enter number2  for issuing a books .....")
        print("....Enter number 3 for return the book and check  for any penalty.....")
        
    elif a=="admin":
        print("\n.....Enter any of the choices given below.....\n")
        print(".....Enter number4  for adding some new books .....")
        print(".....Enter number5  for viewing issued books by user .....\n")
       
    else:
            print("wrong login")
            continue
    
    issued_book=dict()
    issued_book=books
    choices=int(input("Enter any number :"))
    if choices==1 and a=="user":
        print("\n")
        for x in books:
            print(x)
    elif choices==2 and a=="user":
        print("\n Available Books in the Library are given below")
        for x in issued_book.items():
            print(x)
        issuing_book_name=input("\nEnter the book name you want:")
        if issuing_book_name in issued_book and issued_book[issuing_book_name]<=4:
            print("-------This book is already U issued-------")
            print("-------Try another Book---------")
            continue    
        elif issuing_book_name in issued_book and issued_book[issuing_book_name]==5:
            print("---------yes, this book is available---------")
            count=issued_book[issuing_book_name]-1
            issued_book.update({issuing_book_name:count})
            print("--------Your Book is issued successfully------")
        else:
            print("-------Wrong Entry and Book names are case sensitive-----")
            continue
        print("\n---If you want to print the available Books details after issuing a Book ----")
        s=input("\nEnter YES or NO :")
        if s=="YES":
            for x in issued_book.items():
                print(x)
        elif s=="NO":
             continue
        else:
             print("---Wrong Entry---")
            
    elif choices==3 and a=="user":
        returned_book=input("\nEnter the  book name  u returned:")
        if returned_book in issued_book and issued_book[returned_book]==5:
            print("This book is not issued")
        elif returned_book in issued_book and issued_book[returned_book]<=5:       
            count=issued_book[returned_book]+1
            issued_book.update({returned_book:count})
            print("Your book is returned successfully")     
        else:
            print("Wrong Entry ...Book names are case sensitive ")
            continue
        today=datetime.date.today()
        d1=int(d.strftime("%d"))
        today_date_converting=int(today.strftime("%d"))
        c=int(today_date_converting-d1)
        ct=0
        if c>5 and c<=30 :
            ct=c*20
            print("But u are",c,"days late so u will pay..",ct)
        elif c>30 :
            ct=c*20
            print(" You are One month late so u will pay...",ct)     
        else:
            print("congratz u return the book at coorect time")
        
    elif choices==4 and  a=="admin":
        a1=input("\nEnter the new book name:")
        a2=int(input("Enter the number of availablebooks:"))
        a11=dict()
        a11[a1]={a2}
        books.update(a11)
        updated_books.update(a11)
        issued_book.update(a11)
        print("\n")
        for x in books:
            print(x)
    elif ch==5 and a=="admin":
        print("After issuing  Books  its count is given below")
        for x in issued_book.items():
                 print(x)
        print("\n---If you want to print the issued Books only ----")
        s=input("\nEnter YES or NO :")
        if s=="YES":
            diff=dict()
            diff=set(updated_books.items())-set(issued_book.items())
            for x in diff:
                print(x)
        elif s=="NO":
            continue
        else: 
            print("......Wrong Entry......")
        
        
    else: 
         print("......Wrong Entry......")
         print(".......please try again.....")
         i=i+1
         continue
    i=i+1

else:
    print("........Run The Program Again....")

        

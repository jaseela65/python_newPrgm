#Library Management From User and Admin ends 

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


from datetime import datetime, timedelta,date
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
            
            days_to_add=7
            d = datetime.today() + timedelta(days=days_to_add)
            print("\n----You will return this book after 7 dats in this date",d,"----\n----Otherwise U will pay 20rupees per each day----")
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
                 
        else:
            print("Wrong Entry ...Book names are case sensitive ")
            continue
        import datetime
        year = int(input('Enter issued_date  year'))
        month = int(input('Enter issued_date  month'))
        day = int(input('Enter issued_date day'))
        issued_date1 = datetime.date(year, month, day)
        #print(issued_date1)
        today1=datetime.date.today()
        issued_date_converting=int(issued_date1.strftime("%d"))
        today_date_converting=int(today1.strftime("%d"))
        total_days=int(today_date_converting-issued_date_converting)
        days=total_days-7#user penalty will start after 7 days from issued date
        fine=0
        if days>5 and days<=30 :
            fine=days*20
            print("But u are",days,"days late so u will pay..",fine)
        elif days>30 :
            fine=days*20
            print(" You are One month late so u will pay...",fine)
        elif days<0:
            print("enter correct date")
        else:
            print("congratz u return the book at coorect time")
            print("Your book is returned successfully")
        
    elif choices==4 and  a=="admin":
        new_book=input("\nEnter the new book name:")
        new_book_count=int(input("Enter the number of availablebooks:"))
        new_dict=dict()
        new_dict[new_book]={new_book_count}
        books.update(new_dict)
        updated_books.update(new_dict)
        issued_book.update(new_dict)
        print("\n")
        for x in books:
            print(x)
    elif choices==5 and a=="admin":
        print("After issuing  Books  its count is given below")
        for x in issued_book.items():
                 print(x)
        print("\n---If you want to print the issued Books only ----")
        s=input("\nEnter YES or NO :")
        if s=="YES":
            only_issued_book=dict()
            only_issued_book=set(updated_books.items())-set(issued_book.items())
            for x in only_issued_book:
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

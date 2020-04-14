
# write a function to check wheather a string is palindrome or not
def palindrome(s):
    x=s[::-1]
    if s==x:
        print("palindrome")
    else:
        print("not palindrome")

palindrome("abcd")
palindrome("malayalam")

#..............................................................


#write a function to check wheather a number is odd or even

def even(x):
    if x%2==0:
        print(x, "is even number")
    else:
        print(x,"is odd number")

even(10)
even(7)

#...............................................................


#write a function to check wheather a number is positive or negative

def positive(a):
    if a>0:
        print(a,"is positive number")

    else:
        print(a,"is negative number")



positive(34)
positive(-3)

#.................................................................

#get two numbers from user and do below process
#(a+b)(a-b)

def process(a,b):
    x=(a+b)*(a-b)
    print(x)

process(8,2)
process(5,3)

    

#..................................................................

#get three numbers from user and do the below process
#(a+b)(a-b)(a-c)


def operate(a,b,c):
    z=(a+b)*(a-b)*(a-c)
    print(z)

e=int(input("enter no : "))
f=int(input("enter no : "))
g=int(input("enter no : "))
operate(e,f,g)
operate(5,3,2)
















        










        

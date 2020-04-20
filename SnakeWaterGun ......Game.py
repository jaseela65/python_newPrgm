import random
c=["snake","water","gun"]
u=0#user
s=0#system
t=0#tie
i=0
print( "welcome to Snake..Water...Gun....Game")
name=input("Enter your name:")
print("you will enter snake or water or gun")
while i<5:
    n=input()
    b=random.choice(c)
    print(b)
    if n==c[0] and b==c[2]:
        s=s+1
        
    elif n==c[2] and b==c[1]:
        s=s+1
    elif n==c[0] and b==c[1]:
        u=u+1
    elif n==c[2] and b==c[0]:
        u=u+1
    elif n==c[1] and b==c[2]:
        u=u+1
    elif n==c[1] and b==c[0]:
        s=s+1
    elif n== b:
        t=t+1
    else:
        print("wrong entry...Try again..")
        continue
    i=i+1
else:
    print(" Game is over....")
    print(name," won",u,"attempts")
    print("system won",s,"attempts")
    print(t,"attempts are tie")
    
    if s>u and s>t:
        print("Winner is System")
    elif u>s and u>t:
        print("Winner is User",name)
    else:
        print("Try again")
           


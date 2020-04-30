print("..........Welcome To Python Quiz Competition.......\n")
import re
def quiz_login_functtion():
    name=input("Enter your name:")
    mail_id=input("Enter your Email-id :")
    mail_id_pattern='^\w+([\.-]?\w+)*@gmail.com'
    if(re.search(mail_id_pattern,mail_id)):
        return mail_id
    else:
        return "Invalid mail_id..pls try again and give a valid mail id"
         

    print("You can test your Python skills with this Quiz\n")
    print("Here three topics  are available,You can select  any one option for your test\n")
    print("   a, DataStructures in python\n")
    print("   b, Exception Handling\n")
    print("   c, Class and Objects\n")
    option=input("Enter the Option:")
    print("\nNow you can select the Quiz patterns\n")
    print("   1, 5 questions (Related to topic you are selected)\n")
    print("   2, 10 questions (Related to topic you are selected)\n")
    print("   3, 25 questions (This questions are type of above three topics)\n")
    select=input("Enter the Option  from available Quiz patterns:")

def DataStructures_Qustn(number):
    print("   a, DataStructures in python\n")

def Exception_Qustn(number):
    print("   b, Exception Handling\n")
def Class_Qustn(number):
    print("   c, Class and Objects\n")
    
def Mixed_Qustn(number):
    print("   3, 25 questions (This questions are type of above three topics)\n")


total_qustn=0
correct_answr=0
incorrect_answr=0

print(quiz_login_functtion())   

if option=="a" and select==1:
    number=5
    total_qustn,correct_answr,incorrect_answr=DataStructures_Qustn(number)
elif option=="a" and select==2:
    number=10
    total_qustn,correct_answr,incorrect_answr=DataStructures_Qustn(number)
elif option=="b" and select==1:
    number=5
    total_qustn,correct_answr,incorrect_answr=Exception_Qustn(number)
elif option=="b" and select==2:
    number=10
    total_qustn,correct_answr,incorrect_answr=Exception_Qustn(number)
elif option=="c" and select==1:
    number=5
    total_qustn,correct_answr,incorrect_answr=Class_Qustn(number)
elif option=="c" and select==2:
    number=10
    total_qustn,correct_answr,incorrect_answr=Class_Qustn(number)
elif option=="a" or "b" or "c" and select==3:
    number=25
    total_qustn,correct_answr,incorrect_answr=Mixed_Qustn(number)




    




    
    
    


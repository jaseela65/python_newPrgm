print("..........Welcome To Python Quiz Competition.......\n")
import re
import sys
def quiz_login_functtion():
    name=input("Enter your name:")
    mail_id=input("Enter your Email-id :")
    mail_id_pattern='^\w+([\.-]?\w+)*@gmail.com'
    if(re.search(mail_id_pattern,mail_id)):
        return mail_id
    else:
        sys.exit("Invalid mail_id..pls try again and give a valid mail id")
         
def topic():
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
    select=int(input("Enter the Option  from available Quiz patterns:"))
    total_qustn=0
    correct_answr=0
    incorrect_answr=0
    if option=="a" and select==1:
        number=5
        i=0
        while i<5:
            if i==0:
                print("1.Change the value from  'apple'   to   'kiwi' in the fruits list.")
                print("fruits = ['apple', 'banana', 'cherry']")
                print("a, fruits[1]='kiwi'")
                print("b, fruits[0]='kiwi'")
                print("c, fruits[3]='kiwi'")
                print("d, fruits[2]='kiwi'")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="b":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option b: fruits[0]='kiwi'")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==1:
                print("2.Use a range of indexes to print the third, fourth, and fifth item in the list..")
                print("fruits = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')")
                print("a, print(fruits[1:5])")
                print("b, print(fruits[2:6])")
                print("c, print(fruits[2:5])")
                print("d, print(fruits[3:5])")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="c":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option c, print(fruits[2:5])")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif  i==2:
                print("3.Use the remove method to remove 'banana' from the fruits set.")
                print("fruits = {'apple', 'banana', 'cherry'}")
                print("a, remove('banana')")
                print("b, fruits.remove('banana')")
                print("c, fruits('banana')")
                print("d, fruits,remove('banana')")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="b":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option b, fruits.remove('banana')")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==3:
                print("4. Change the 'year' value from 1964 to 2020.")
                print('''car =	{"brand": "Ford","model": "Mustang","year": 1964}''')
                print("a, car['year']=2020")
                print("b, ['year']=2020")
                print("c, 'year'=2020")
                print("d, ['year']car =2020")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="a":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option a, car['year']=2020")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==4:
                print("5.Use the clear method to empty the car dictionary.")
                print('''car =	{"brand": "Ford","model": "Mustang","year": 1964}''')
                print("a, car.clear()")
                print("b, clear()")
                print("c, car,clear()")
                print("d, car:clear()")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="a":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option b, fruits.remove('banana')")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
        else:
            print("Your Test Is completed")
            print("---Total oquestions=",total_qustn,"---")
            print("You got",correct_answr,"points")
            print(incorrect_answr,"Answers are Incorrect")  
                
#......................................................................................................                
                
    elif option=="a" and select==2:
        number=10
        i=0
        while i<10:
            if i==0:
                print("1.Change the value from  'apple'   to   'kiwi' in the fruits list.")
                print("fruits = ['apple', 'banana', 'cherry']")
                print("a, fruits[1]='kiwi'")
                print("b, fruits[0]='kiwi'")
                print("c, fruits[3]='kiwi'")
                print("d, fruits[2]='kiwi'")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="b":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option b: fruits[0]='kiwi'")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==1:
                print("2.Use a range of indexes to print the third, fourth, and fifth item in the list..")
                print("fruits = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')")
                print("a, print(fruits[1:5])")
                print("b, print(fruits[2:6])")
                print("c, print(fruits[2:5])")
                print("d, print(fruits[3:5])")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="c":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option c, print(fruits[2:5])")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif  i==2:
                print("3.Use the remove method to remove 'banana' from the fruits set.")
                print("fruits = {'apple', 'banana', 'cherry'}")
                print("a, remove('banana')")
                print("b, fruits.remove('banana')")
                print("c, fruits('banana')")
                print("d, fruits,remove('banana')")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="b":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option b, fruits.remove('banana')")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==3:
                print("4. Change the 'year' value from 1964 to 2020.")
                print('''car =	{"brand": "Ford","model": "Mustang","year": 1964}''')
                print("a, car['year']=2020")
                print("b, ['year']=2020")
                print("c, 'year'=2020")
                print("d, ['year']car =2020")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="a":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option a, car['year']=2020")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==4:
                print("5.Use the clear method to empty the car dictionary.")
                print('''car =	{"brand": "Ford","model": "Mustang","year": 1964}''')
                print("a, car.clear()")
                print("b, clear()")
                print("c, car,clear()")
                print("d, car:clear()")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="a":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option b, fruits.remove('banana')")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==5:
                print("6.Use negative indexing to print the last item in the list.")
                print('''fruits = ["apple", "banana", "cherry"]''')
                print("a, print(fruits[-3])")
                print("b, print(fruits[-2])")
                print("c, print(fruits[0])")
                print("d, print(fruits[-1])")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="d":
                    correct_answr=correct_answr+1
                    print("\ncorrect Answer")
                else:
                    print("\nWrong Answer.....correct answer is option d, print(fruits[-1])")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==6:
                print("7.Use the correct syntax to print the number of items in the fruits tuple.")
                print('''fruits = ("apple", "banana", "cherry")''')
                print("a, print(len(fruits))")
                print("b, print(items(fruits))")
                print("c, print(count(fruits))")
                print("d, print(fruits)")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="a":
                    correct_answr=correct_answr+1
                    print("\ncorrect Answer")
                else:
                    print("\nWrong Answer.....correct answer is option a, print(len(fruits))")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
                
        else:
            
            print("total oquestions=",total_qustn)
            print("correct=",correct_answr)
            print("Incorrect=",incorrect_answr)  
                
    
    elif option=="b" and select==1:
        number=5
    
    elif option=="b" and select==2:
        number=10
    
    elif option=="c" and select==1:
        number=5
    
    elif option=="c" and select==2:
        number=10
    
    elif option=="a" or "b" or "c" and select==3:
        number=25
    else:
         print("wrong Entry")
    
        
total_qustn=0
correct_answr=0
incorrect_answr=0

mail_id=quiz_login_functtion()
topic()


    

    








    




    
    
    


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
    print("   b, if...else.statemebts,For loops and While loops\n")
    print("   c, Class and Objects\n")
    print("   d, Mixed type questions from whole python,contains 25 questions only\n")
    option=input("Enter the Option:")
    print("\nNow you can select the Quiz patterns\n")
    print("   1, 5 questions (Related to topic you are selected)\n")
    print("   2, 10 questions (Related to topic you are selected)\n")
    print("   3, 25 questions (This questions are Mixed type of questions)\n")
    select=int(input("Enter the Option  from available Quiz patterns:"))
    total_qustn=0
    correct_answr=0
    incorrect_answr=0
    if option=="a" and select==1:
        number=5
        i=0
        while i<5:
            if i==0:
                print("\n1.Change the value from  'apple'   to   'kiwi' in the fruits list.")
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
                print("\n2.Use a range of indexes to print the third, fourth, and fifth item in the list..")
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
                print("\n3.Use the remove method to remove 'banana' from the fruits set.")
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
                print("\n4. Change the 'year' value from 1964 to 2020.")
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
                print("\n5.Use the clear method to empty the car dictionary.")
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
            print("\n---Your Test Is completed---")
            print("---Total oquestions=",total_qustn,"---")
            print("---You got",correct_answr,"points")
            print("---",incorrect_answr,"Answers are Incorrect---")  
                

#......................................................................................................                
                
    elif option=="a" and select==2:
        number=10
        i=0
        while i<10:
            if i==0:
                print("\n1.Change the value from  'apple'   to   'kiwi' in the fruits list.")
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
                print("\n2.Use a range of indexes to print the third, fourth, and fifth item in the list..")
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
                print("\n3.Use the remove method to remove 'banana' from the fruits set.")
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
                print("\n4. Change the 'year' value from 1964 to 2020.")
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
                print("\n5.Use the clear method to empty the car dictionary.")
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
                print("\n6.Use negative indexing to print the last item in the list.")
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
                print("\n7.Use the correct syntax to print the number of items in the fruits tuple.")
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
            elif i==7:
                print("\n8.Use the correct method to add multiple items (more_fruits) to the fruits set.")
                print('''fruits = {"apple", "banana", "cherry"}\nmore_fruits = ["orange", "mango", "grapes"]''')
                print("a, fruits.add(more_fruits)")
                print("b, fruits.update(more_fruits)")
                print("c, fruits.extend(more_fruits)")
                print("d, fruits.insert(more_fruits)")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="b":
                    correct_answr=correct_answr+1
                    print("\ncorrect Answer")
                else:
                    print("\nWrong Answer.....correct answer is option b, fruits.update(more_fruits)")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==8:
                print("\n9.Use the discard method to remove 'banana' from the fruits set.")
                print('''fruits = {"apple", "banana", "cherry"}''')
                print("a, fruits.discard('banana')")
                print("b, fruits.remove('banana')")
                print("c, fruits,discard('banana')")
                print("d, fruits.delete('banana')")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="a":
                    correct_answr=correct_answr+1
                    print("\ncorrect Answer")
                else:
                    print("\nWrong Answer.....correct answer is option a, fruits.discard('banana')")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==9:
                print("\n10.Add the key/value pair 'color' : 'red' to the car dictionary.")
                print('''car =	{"brand": "Ford","model": "Mustang","year": 1964}''')
                print("a, car('color')='red'")
                print("b, car['color']='red'")
                print("c, car.['color']='red'")
                print("d, car,['color']='red'")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="b":
                    correct_answr=correct_answr+1
                    print("\ncorrect Answer")
                else:
                    print("\nWrong Answer.....correct answer is option b, car['color']='red'")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1   
                
        else:
            print("\n---Your Test Is completed---")
            print("---Total oquestions=",total_qustn,"---")
            print("---You got",correct_answr,"points")
            print("---",incorrect_answr,"Answers are Incorrect---")  
                

#....................................................................................................                
    
    elif option=="b" and select==1:
        number=5
        i=0
        while i<5:
            if i==0:
                print("\n1.Print 'Hello World' if a is not equal to b.")
                print("a = 50\nb = 10\n__ a __ b_\n  print('Hello World')")
                print("\na, if a!=b:\nb, if a==b:\nc, if a not b:\nd, if a!=b")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="a":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option a, if a!=b:")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==1:
                print("\n2. Print 'Hello' if a is equal to b, and c is equal to d.")
                print("if a == b ___ c==d:\n  print('Hello')")
                print("\na, if a == b not c==d:\nb, if a == b and c==d:\nc, if a == b == c==d:\nd, if a == b and c==d")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="b":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option b, if a == b and c==d:")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif  i==2:
                print("\n3. Print i as long as i is less than 6.")
                print("i=1\n_____ i<6_\n print(i)\n i+= 1")
                print("\na, while i<6:\nb, if i<6:\nc, while i<6\nd, for i<6:")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="a":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option a, while i<6:")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==3:
                print("\n4. Which is used for Stop the loop if i is 3.")
                print('''i = 1\nwhile i < 6:\n if i == 3:\n  _____\n i+=1''')
                print("a, continue\nb, stop\nc, break\nd, not")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="c":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option c, break")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==4:
                print("\n5.In the loop, _____ is used to jump directly to the next iteration.")
                print("a, continue\nb, stop\nc, break\nd, not")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="a":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option a, continue")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
        else:
            print("\n---Your Test Is completed---")
            print("---Total oquestions=",total_qustn,"---")
            print("---You got",correct_answr,"points")
            print("---",incorrect_answr,"Answers are Incorrect---")  
                
#......................................................................................................                
                
    
    elif option=="b" and select==2:
        number=10
        i=0
        while i<10:
            if i==0:
                print("\n1.Print 'Hello World' if a is not equal to b.")
                print("a = 50\nb = 10\n__ a __ b_\n  print('Hello World')")
                print("\na, if a!=b:\nb, if a==b:\nc, if a not b:\nd, if a!=b")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="a":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option a, if a!=b:")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==1:
                print("\n2. Print 'Hello' if a is equal to b, and c is equal to d.")
                print("if a == b ___ c==d:\n  print('Hello')")
                print("\na, if a == b not c==d:\nb, if a == b and c==d:\nc, if a == b == c==d:\nd, if a == b and c==d")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="b":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option b, if a == b and c==d:")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif  i==2:
                print("\n3. Print i as long as i is less than 6.")
                print("i=1\n_____ i<6_\n print(i)\n i+= 1")
                print("\na, while i<6:\nb, if i<6:\nc, while i<6\nd, for i<6:")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="a":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option a, while i<6:")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==3:
                print("\n4. Stop the loop if i is 3.")
                print('''i = 1\nwhile i < 6:\n if i == 3:\n  _____\n i+=1''')
                print("a, continue\nb, stop\nc, break\nd, not")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="c":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option c, break")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==4:
                print("\n5.In the loop, _____ is used to jump directly to the next iteration.")
                print("a, continue\nb, stop\nc, break\nd, not")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="a":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option a, continue")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==5:
                print("\n6.In if... statements ____  statement is used  to avoid getting an error?")
                print("a, continue\nb, stop\nc, pass\nd, break")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="c":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option c, pass")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==6:
                print("\n7.which is the correct example for ShortHand if..statements?.")
                print("a, if a > b: print('a is greater than b)\nb, if a > b:\n print('a is greater than b')")
                print("c, if a > b:\nprint('a is greater than b)\nd, if a > b:\n print a is greater than b ")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="a":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option a, if a > b: print('a is greater than b)")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==7:
                print("\n8.Which keyword is used for Print a message once the condition is false.")
                print("i = 1\nwhile i < 6:\n print(i)\n i += 1\n____\n  print('i is no longer less than 6')")
                print("a, continue\nb, else\nc, break\nd, not")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="b":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option b, else")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==8:
                print("\n9.Loop through the items in the fruits list.")
                print("fruits = ['apple', 'banana', 'cherry']\n___ x __ fruits:\n print(x)")
                print("a, for x in fruits\nb, while x in fruits\nc, if x in fruits\nd, else x in fruits")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="a":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option b, a, for x in fruits")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
            elif i==9:
                print("\n10.Use the range function to loop through a code set 6 times.")
                print("for x in _________:\n print(x)")
                print("a, range(6)\nb, range 6\nc, (6)range\nd, range")
                answer=input("Enter the answer from the above option:")
                answer.lower()
                if answer=="a":
                    correct_answr=correct_answr+1
                    print("correct Answer")
                else:
                    print("Wrong Answer.....correct answer is option b, a, range(6)")
                    incorrect_answr=incorrect_answr+1
                total_qustn=total_qustn+1
                i=i+1
                                
        else:
            print("---Your Test Is completed---")
            print("---Total oquestions=",total_qustn,"---")
            print("---You got",correct_answr,"points---")
            print("---",incorrect_answr,"Answers are Incorrect---")  
         
#.........................................................................                
                
    
    elif option=="c" and select==1:
        number=5
    
    elif option=="c" and select==2:
        number=10
    
    elif option=="d" and select==3:
        number=25
    else:
         print("wrong Entry")
    
        
total_qustn=0
correct_answr=0
incorrect_answr=0

mail_id=quiz_login_functtion()
topic()


    

    








    




    
    
    


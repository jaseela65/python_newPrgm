print("..........Welcome To Python Quiz Competition.......\n")
import re
import sys
def quiz_login_functtion():
    name=input("Enter your name:")
    mail_id=input("Enter your Email-id :")
    mail_id_pattern='^\w+([\.-]?\w+)*@gmail.com'
    if(re.search(mail_id_pattern,mail_id)):
        return "---Login sucessfully---"
    else:
        sys.exit("Invalid mail_id..pls try again and give a valid mail id")
         

main = {
         1:
      {
        "question":["1.What is a correct syntax to output 'Hello World' in Python?","select any option given below"],
        "options":["a, echo('Hello World');","b, echo('Hello World')","c, print('Hello World')","d, p('Hello World')"],
        "correct answer":"c",
        "explanation":"correct answer is c, print('Hello World')"
      },
         2:
      {
        "question":["2.How do you insert COMMENTS in Python code?","select any option given below"],
        "options":["a, #This is a comment","b, //This is a comment","c, /*This is a comment*/","d, */This is a comment"],
        "correct answer":"a",
        "explanation":"correct answer is a, #This is a comment"
      },
         3:
      {
        "question":["3.Change the value from  'apple'   to   'kiwi' in the fruits list","fruits = ['apple', 'banana', 'cherry']"],
        "options":["a, fruits[1]='kiwi'","b, fruits[0]='kiwi'","c, fruits[3]='kiwi'","d, fruits[2]='kiwi'"],
        "correct answer":"b",
        "explanation":"correct answer is b, fruits[0]='kiwi'"
      },
         4:
      {
          "question":["4.Use a range of indexes to print the third, fourth, and fifth item in the list..","fruits = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')"],
          "options":["a, print(fruits[1:5])","b, print(fruits[2:6])","c,  print(fruits[2:5])","d, print(fruits[3:5])"],
          "correct answer":"c",
          "explanation":"correct answer is c,  print(fruits[2:5])"
      },
         5:
      {
          "question":["5.Use the remove method to remove 'banana' from the fruits set.","fruits = {'apple', 'banana', 'cherry'}"],
          "options":["a, remove('banana')","b, fruits.remove('banana')","c, fruits('banana')","d, fruits,remove('banana')"],
          "correct answer":"b",
          "explanation":"correct answer is c, b, fruits.remove('banana')"
      },
         6:
      {
          "question":["6.in Dictionary Change the 'year' value from 1964 to 2020.","car =	{'brand': 'Ford','model': 'Mustang','year': 1964}"],
          "options":["a, car['year']=2020","b, ['year']=2020","c, 'year'=2020","d, ['year']car =2020"],
          "correct answer":"a",
          "explanation":"correct answer is a, car['year']=2020"
      },
         7:
      {
          "question":["7.Use the clear method to empty the car dictionary.","car ={'brand': 'Ford','model': 'Mustang','year': 1964}"],
          "options":["a, car.clear()","b, clear()","c, car,clear()","d, car:clear()"],
          "correct answer":"a",
          "explanation":"correct answer is a, car.clear()"
      },
          8:
      {
          "question":["8.Use the correct syntax to print the number of items in the fruits tuple ?","fruits = ('apple', 'banana', 'cherry')"],
          "options":["a, print(fruits)","b, print(items(fruits))","c, print(count(fruits))","d, print(len(fruits))"],
          "correct answer":"d",
          "explanation":"correct answer is d, print(len(fruits))"
      },
          9:
      {
          "question":["9.What is the correct file extension for Python files?","select any option given below.."],
          "options":["a, .py","b, .pyth","c, .pt:","d, .pyt"],
          "correct answer":"a",
          "explanation":"correct answer is a, if .py"
      },
           10:
      {
          "question":["10.What is the correct syntax to output the type of a variable or object in Python?","select any option given below.."],
          "options":["a, print(typeOf(x))","b, print(type(x))","c, print(typeof(x))","d, print(type of x))"],
          "correct answer":"b",
          "explanation":"correct answer is b, print(type(x))"
      },
          11:
      {
          "question":["11.What is the correct way to create a function in Python?","select any option given below.."],
          "options":["a, function myfunction():","b, create myFunction():","c, def myFunction():","d, myFunction def():"],
          "correct answer":"c",
          "explanation":"correct answer is c, def myFunction():"
      },
          12:
      {
          "question":["12.Which method can be used to remove any whitespace from both the beginning and the end of a string?","select any option given below.."],
          "options":["a, len()","b, ptrim()","c, trim()","d, strip()"],
          "correct answer":"d",
          "explanation":"correct answer is d, strip()"
      },
          13:
      {
          "question":["13.Which operator is used to multiply numbers?","select any option given below.."],
          "options":["a, % ","b, x ","c, * ","d, # "],
          "correct answer":"c",
          "explanation":"correct answer is c, * "
      },
          14:
      {
          "question":["14.Which collection is ordered, changeable, and allows duplicate members?","select any option given below.."],
          "options":["a, SET ","b, LIST ","c, TUPLE ","d, DICTIONARY "],
          "correct answer":"b",
          "explanation":"correct answer is b, LIST "
      },
         15:
      {
          "question":["15.Which statement is used to stop a loop?","select any option given below.."],
          "options":["a, break ","b, return ","c, stop ","d, exit "],
          "correct answer":"a",
          "explanation":"correct answer is a, break"
      }
    }
#print(main)
total_qustn=0
correct_answr=0
incorrect_answr=0
print(quiz_login_functtion())
print("\nNow you can select the Quiz patterns\n")
print("    5 questions \n")
print("    10 questions \n")
print("    25 questions \n")
select=int(input("Enter the Option  from available Quiz patterns:"))
for i in range(1,select):
    print(main[i]["question"][0])
    print(main[i]["question"][1])
    print(main[i]["options"][0])
    print(main[i]["options"][1])
    print(main[i]["options"][2])
    print(main[i]["options"][3])
    x=input()
    x.lower()
    if x== main[i]["correct answer"]:
        correct_answr=correct_answr+1
        print("--Correct Answer---")
               
    else:
        incorrect_answr=incorrect_answr+1
        print("wrong Answer")
        print(main[i]["explanation"])
   
else:
    print("correct:",correct_answr)
    


from random import shuffle
print("=======================================================***)WELCOME(***==========================================================")
# In this version I will be using dictionaries and list to create my gk quiz.
print("Welcome To General Knowledge Rules and Skills Quiz")
import datetime
x=datetime.datetime.now()
print(x)
print("--------------------------------------------------------------")

#Creating dictionary for question and the right answer

#Using functions to greet the user.



def greet():
    
    while True:
        name = input("What's your name? : ")
        if name.isalpha():
            break
        print("Please enter characters A-Z only")
greet()


#Asking the user to enter their age by using try and except.

try:
    age=int(input("How old are you?:"))
except:
    print("This is not a valid data type.Please enter your age in numbers.")
    age=int(input("How old are you?:"))


#Asking the user the enter their year level using try and except.

try:
    yearlevel=int(input("Enter your year level:"))
except:
    print("This is not a valid data type. Please enter your age in numbers.")
    age=int(input("How old are you?:"))



#Asking the user if they are ready for the quiz

ready=input("Are you ready for the quiz?: press y to continue or x to exit:")

if ready=="y" or ready == "yes" :
    print("lets continue")
    print("---------------------------------------------")
    print("Please answer the questions with the the alphabets (a,b,c,d)")
    print("---------------------------------------------")
elif ready== "x" :  #If the user inputs x or no, when they are asked if they want to contiue the quiz or not.
    print("Consider playing later")
elif ready== "no":
    print ("Consider playing later ")

def get_range():
    global num, total
    while True:
        try:
            num = int(input("Please enter the amount of rounds you'd like to play : "))
            if 0<num<=5:
                total=num
                break
            else:
                print("The max is 5")
        except:
            pass
       
get_range()


gkquiz = [
    [
     'What is the capital of France?',
     {'answer':'c','option':'a)India:b)London:c)Paris'}
     ],
    [
     'What is the capital of Pakistan?',
     {'answer':'a','option':'a)islamabad:b)London:c)China'}
     ],
    [
     'What is the capital of New zealand?',
     {'answer':'c','option':'a)Fijji:b)America:c)Wellington'}
     ],
    [
     'What is the capital of America?',
     {'answer':'a','option':'a)Washington:b)new zealand:c)Australia'}
     
     ],
    [
     'What is the capital of Turkey?',
     {'answer':'b','option':'a)Mumbai:b)Ankara:c)Pakistan'}
     
     ],
    ]
shuffle(gkquiz)
index=0
score=0
optnum=0

while True:
    while num>0:
        data = gkquiz[0]
        q=data[0]
        data = data[1]
        answer = data['answer']
        option = data['option']

        print(q)
        print(option)     
        while True:
            user_answer = input("Please enter you answer here :")
            if user_answer == 'a' or user_answer == 'b' or user_answer == 'c':
                if user_answer == answer:
                    print("**********************")
                    print("Nailed it, keep it up!")
                    print("**********************")
                    score +=1
                    print("**********************")
                    print("Your score is", score)
                    print("**********************")
                else:
                    print("********************************************************************************")
                    print("Wrong! Sorry but the option you have chosen is incorrect. The right answer is",answer)
                    print("********************************************************************************")
                del gkquiz[0]
                num-=1
                break
            else:
                print("Please enter your answer in a,b,c only")

               

print("Your score is",score,"out of 10 points")  #Presenting the scores to the users.
print("Quiz Complete, WELL DONE :)")
exit()

    



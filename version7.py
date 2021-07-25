
#score mechanics
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

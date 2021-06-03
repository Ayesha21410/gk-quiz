print("----------------------------------------------------------------------------------------------------------")
print("please answer the questions with the alphabets(a,b,c,d)")
print("----------------------------------------------------------------------------------------------------------")

#Question for General knowledgeQuiz
for q in generalknowledgequiz.keys():
    print(q) #printing one question at a time in order.
    print(optlist[index]) #print first option.
    index=index+1
    
    user_ans=input("Enter your answer")
    answer = gkquiz[q] #Finding the answer to the question in the dictionary.

    if user_ans==answer:
        print("That is correct,keep up the great work")
        print("--------------------------------------")
        score=score+1
        print("score",score+0)
        
    else:
        print("That is not correct.The answer is",answer)
        print("---------------------------------------")
       

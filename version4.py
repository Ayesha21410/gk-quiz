#Asking user's if they want to know the rules of game?
def rules():
    rules = input("Do you want to read the rules? press 'y' for rules or 'n' to continue : ")
    if rules == 'yes' or rules == 'y':
        print("To play you will be ask how many rounds you would want to play. /n Once you have \nchosen your rounds you will recive questions to answer./nEvery question you get \ncorrect you will earn 1 point if you get any question incorrect you wont recive any points. Enjoy the game!")
    else:
        print("You may continue without the rules.")
rules()




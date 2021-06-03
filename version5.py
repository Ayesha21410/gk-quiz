
#asking user how many round they would like to play
def get_range():
    global num, total
    while True:
        try:
            num = int(input("Please enter the amount of rounds you'd like to play : "))
            if 0<num<=5 :
                total=num
                print("got it.")
                
                break
            else:
                print("The max is 5")
        except:
            pass
       
get_range()

print("----------------")
age = int(input("please enter your age : "))
if (age<7) :
    print(" the minimum age that require is greater than7 or less than 100. you should be more than 7 years old.")
    age = int(input("Please enter your age : "))
elif age>=7 and age<=100:
    print("thanks")
elif age>=100 :
    print("the minimum age that require is greater than7 or less than 100. you should be less than 100 years old.")
    age = int(input("Please enter your age : "))
else:
    print("Thanks")

#Asking users name.
print("welcome to my quiz")
#Ask for name
while True:
    name = input("Enter your name : ")
    if name.isalpha():
        break
    print("please enter characters A-Z only")

print('hello',name)

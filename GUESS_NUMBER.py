import random

target =random.randint(1,100)

while True:
    userChoice=(input("guess the target or quit(Q):"))
    if (userChoice == "Q"):
        break
    userChoice=int(userChoice)
    if (userChoice==target):
        print("Success : correct Guess!")
        break
    elif(userChoice<target):
        print("your number was too small Guess bigger number")
    else:
         print("your number was too big Guess smaller number")
         
print("---------GAME OVER----------")
        
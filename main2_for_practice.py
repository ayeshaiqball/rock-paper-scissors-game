import random

'''
1 for rock
2 for scissor
3 for paper
'''
computer=random.choice([1,2,3])

youstr=input("Enter your choice (r for rock and s for scissor and p for paper): ")

youdict={ "r":1, "s":2, "p":3 }

reversedict={1:"Rock",2:"Scissor",3:"Paper"}

you=youdict[youstr]

print(f"You entered {reversedict[you]}\n Computer entered {reversedict[computer]}")

if(computer==you):
    print("Its a draw!")
else:
    if(computer==1 and you==2):
        print("Computer win!")
    elif(computer==1 and you==3):
        print("You win!")
    elif(computer==2 and you==1):
        print("You win!")
    elif(computer==2 and you==3):
        print("Computer win!")
    elif(computer==3 and you==1):
        print("Computer win!")
    elif(computer==3 and you==2):
        print("You win!")
    else:
        print("Something went wrong!")

    # I made this by myself
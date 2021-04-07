# STONE PAPER SCISSOR
# Between player and computer
import random

# COMPUTER ---
computer = None
my_list = ["Stone","Paper","Scissor"]
random.shuffle(my_list)
computer = random.choice(my_list)


# PLAYER ---
player = int(input("Enter 1(Stone) 2(Paper) 3(Scissor): "))

while True:
    if player == int(1):
        player = "Stone"
        break
    elif player == int(2):
        player = "Paper"
        break
    elif player == int(3):
        player = "Scissor"
        break
    else:
        player = int(input("Enter 1(Stone) 2(Paper) 3(Scissor): "))

print("Computer =",computer)
print("Player =",player)  



# Wanna try again?
def myfunc(ask):
    if ask == "y":
        player = int(input("Enter 1(Stone) 2(Paper) 3(Scissor): "))
    elif ask == "n":
        print("Thanks for playing!")



# Condition Statements ---
while True:
    if computer == player:
        print("It's a Tie!")
        myfunc(ask = str(input("Do you wanna try again? y/n? ")))
        break

    elif computer == "Stone" and player == "Paper":
        print("Player Won!")
        myfunc(ask = str(input("Do you wanna try again? y/n? ")))
        break

    elif computer == "Stone" and player == "Scissor":
        print("Computer Won!")
        myfunc(ask = str(input("Do you wanna try again? y/n? ")))
        break

    elif computer == "Paper" and player == "Stone":
        print("Computer Won!")
        myfunc(ask = str(input("Do you wanna try again? y/n? ")))
        break

    elif computer == "Paper" and player == "Scissor":
        print("Player Won!")
        myfunc(ask = str(input("Do you wanna try again? y/n? ")))
        break

    elif computer == "Scissor" and player == "Stone":
        print("Player Won!")
        myfunc(ask = str(input("Do you wanna try again? y/n? ")))
        break

    elif computer == "Scissor" and player == "Paper":
        print("Computer Won!")
        myfunc(ask = str(input("Do you wanna try again? y/n? ")))
        break


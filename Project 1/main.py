import random

computer = random.choice([0,1,-1])
print("lets play a game of Rock Paper Scissors\nChose r = Rock , p = Paper and s = Scissors ")
youstr = input("Enter your choice : ")
print("-------------------------")

youDist = {
    "r" : 0,
    "p" : 1,
    "s" : -1
}
reverseDist = {
    0 : "Rock",
    1 : "Paper",
    -1 : "Scissors"
}

you = youDist[youstr]

print(f"Computer chose {reverseDist[computer]}\nYou chose {reverseDist[you]}")
print("-------------------------")


if(computer == you):
    print("Its a Draw")

elif(computer == 0 and you == 1):
    print("You win!")
elif(computer == 0 and you == -1):
    print("You lose!")
    print("Try Again :-)")
elif(computer == 1 and you == 0 ):
    print("You lose!")
    print("Try Again :-)")
elif(computer == 1 and you == -1):
    print("You win!")
elif(computer == -1 and you == 0):
    print("You win!")
elif(computer == -1 and you == 1):
    print("You lose!")
    print("Try Again :-)")
else:
    print("Something went wrong!")
                
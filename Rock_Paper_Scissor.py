import random

user_wins=0
computer_wins=0

options=["rock","paper","sissor"]

while True:
    user_input=input("Type Rock/Paper/sissor or Q to quit :) ").lower()
    if user_input=="q":
        break

    if user_input not in options:
        continue

    random_num=random.randint(0,2) # where 0=rock, 1=paper, 2=sissor
    computer_pick=options[random_num]
    print("Computer picked", computer_pick +".")

    if user_input=="rock" and computer_pick=="sissor":
        print("You Won!!")
        user_wins=user_wins+1
    
    elif user_input=="Paper" and computer_pick=="rock":
        print("You Won!!")
        user_wins=user_wins+1

    elif user_input=="sissor" and computer_pick=="paper":
        print("You Won!!")
        user_wins=user_wins+1
    
    else:
        print("You Loose 0_0")
        computer_wins=computer_wins+1

print("You won", user_wins, "times :)")
print("Computer wins", computer_wins, "times :)")
if user_wins>=computer_wins:
    print("Good job!! you are master in this :)")
print("Goodbye!!")

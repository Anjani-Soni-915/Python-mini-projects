print("Welcome to my quiz game!")

playing = input("Do you want to play this game? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play the game :) ")
score = 0

answer = input("What is the full form of 'CPU'? ")
if answer.lower() == "central processing unit":
    print("Correct :)")
    score = score+1
else:
    print("Incorrect :(")

answer = input("Which is the first fully supported 64-bit operating system? ")
if answer.lower() == "linux":
    print("Correct :)")
    score = score+1
else:
    print("Incorrect :(")

answer = input("In computer world, Trojan refers to? ")
if answer.lower() == "malware":
    print("Correct :)")
    score = score+1
else:
    print("Incorrect :(")


answer = input("which protocol is used to recieve an e-mail? ")
if answer.lower() == "pop3":
    print("Correct :)")
    score = score+1
else:
    print("Incorrect :(")

answer = input("which computer program converts assembly language to machine language? ")
if answer.lower() == "assembler":
    print("Correct :)")
    score = score+1
else:
    print("Incorrect :(")


print("Your Scores 0_0 ")
print("you got " + str(score) + " out of 5")
if score == 5:
    print("CONGRATS ^_^")
print("you got " + str((score/5)*100)+"%")

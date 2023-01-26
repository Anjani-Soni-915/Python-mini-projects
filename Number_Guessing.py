import random
top_most_range = input("Enter the number: ")

if top_most_range.isdigit():
    top_most_range = int(top_most_range)

    if top_most_range <= 0:
        print("Please enter the number larger than 0 next time.")
        quit()

else:
    print("Please ente the nmber next time.")
    quit()

random_num = random.randint(0, top_most_range)
gussess = 0

while True:
    gussess = gussess+1
    user_guess = input("Make a guess :) ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time ^_^")
        continue

    if user_guess == random_num:
        print("Congratulations! You got it :)")
        break
    elif user_guess > random_num:
        print("You were above the number ^_^ ")
    else:
        print("You were below the number ^_^ ")

print("You got it in", gussess, "gussess :-)")

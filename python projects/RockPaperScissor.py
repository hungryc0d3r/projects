# Computer vs Player

# variables -> computer_score, Player_score
# computer score -> random select
# using choice from random module

import random

# enter num to play no of times you need
N = int(input("No of times to play! "))
n = 1    # Iterating on guesses

if N > 0:
    while True:
        C_choice = random.choice(["r", "p", "s"])
        P_choice = input("Your choice please: ")

        C_score = 0
        P_score = 0

        if C_choice == P_choice:
            C_score += 0
            P_score += 0

        elif C_choice == "r" and P_choice == "p":
            C_score += 0
            P_score += 1

        elif C_choice == "r" and P_choice == "s":
            C_score += 1
            P_score += 0

        elif C_choice == "p" and P_choice == "r":
            C_score += 1
            P_score += 0

        elif C_choice == "p" and P_choice == "s":
            C_score += 0
            P_score += 1

        elif C_choice == "s" and P_choice == "r":
            C_score += 0
            P_score += 1

        elif C_choice == "s" and P_choice == "p":
            C_score += 1
            P_score += 0

        if n >= N:
            break
        n += 1
else:
    print("You have entered Wrong Number!! Enter the +ve number only!")


print("<<<<------ Results ------>>>>")

# results
if C_score > P_score:
    print("\t Computer is winner!")

elif C_score < P_score:
    print("\t Player is winner!")

else:
    print("\t DRAW")

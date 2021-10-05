# guess the number in 10 guesses
# randrange(a, b+1)   usage randrange

import random

guessNum = random.randrange(1,101)

n = 1
c = 10

while True:
    if n==1:
        number = int(input('number to be guessed: '))
        if number == guessNum:
            print("You have guessed the number correctly!")
            break
        elif number < guessNum:
            print("The number is lesser than the gussing number!")
        else:
            print("The number is greater than the guessing number!")
            
        print(f"{c-n}  Chances left!")
        
    elif n == 2:
        number = int(input('number to be guessed: '))
        if number == guessNum:
            print("You have guessed the number correctly!")
            break
        elif number < guessNum:
            print("The number is lesser than the gussing number!")
        else:
            print("The number is greater than the guessing number!")
            
        print(f"{c-n}  Chances left!")
        
    elif n == 3:
        number = int(input('number to be guessed: '))
        if number == guessNum:
            print("You have guessed the number correctly!")
            break
        elif number < guessNum:
            print("The number is lesser than the gussing number!")
        else:
            print("The number is greater than the guessing number!")
            
        print(f"{c-n}  Chances left!")
        
    elif n == 4:
        number = int(input('number to be guessed: '))
        if number == guessNum:
            print("You have guessed the number correctly!")
            break
        elif number < guessNum:
            print("The number is lesser than the gussing number!")
        else:
            print("The number is greater than the guessing number!")
            
        print(f"{c-n}  Chances left!")
        
    elif n == 5:
        number = int(input('number to be guessed: '))
        if number == guessNum:
            print("You have guessed the number correctly!")
            break
        elif number < guessNum:
            print("The number is lesser than the gussing number!")
        else:
            print("The number is greater than the guessing number!")
            
        print(f"{c-n}  Chances left!")
        
    elif n == 6:
        number = int(input('number to be guessed: '))
        if number == guessNum:
            print("You have guessed the number correctly!")
            break
        elif number < guessNum:
            print("The number is lesser than the gussing number!")
        else:
            print("The number is greater than the guessing number!")
            
        print(f"{c-n}  Chances left!")
        
    elif n == 7:
        number = int(input('number to be guessed: '))
        if number == guessNum:
            print("You have guessed the number correctly!")
            break
        elif number < guessNum:
            print("The number is lesser than the gussing number!")
        else:
            print("The number is greater than the guessing number!")
            
        print(f"{c-n}  Chances left!")
        
    elif n == 8:
        number = int(input('number to be guessed: '))
        if number == guessNum:
            print("You have guessed the number correctly!")
            break
        elif number < guessNum:
            print("The number is lesser than the gussing number!")
        else:
            print("The number is greater than the guessing number!")
            
        print(f"{c-n}  Chances left!")
        
    elif n == 9:
        number = int(input('number to be guessed: '))
        if number == guessNum:
            print("You have guessed the number correctly!")
            break
        elif number < guessNum:
            print("The number is lesser than the gussing number!")
        else:
            print("The number is greater than the guessing number!")
            
        print(f"{c-n}  Chances left!")
    
    elif n == 10:
        number = int(input('number to be guessed: '))
        if number == guessNum:
            print("You have guessed the number correctly!")
            break
        elif number < guessNum:
            print("The number is lesser than the gussing number!")
        else:
            print("The number is greater than the guessing number!")
            
        print(f"{c-n}  Chances left!")
    
    if n > 10:
        print("Better luck next time!")
        break
    n += 1
    


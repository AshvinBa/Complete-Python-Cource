import random

randNumber = random.randint(1,100)
userGuess = None
guesses = 0

while(randNumber != userGuess) :
    userGuess = int(input("Enter the Guessing Number: "))
    guesses +=1
    
    if(userGuess == randNumber):
        print(f"Congratulations! You have guessed the number in {guesses} guesses. ")
    else:
        if(userGuess < randNumber):
            print("Too Low! guess again Larger than this.")
        else:
            print("Too High! Guess again Smaller than this.")
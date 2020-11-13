
# pip install random-word
import math
import time
from random_word import RandomWords

r = RandomWords()

def new_game():
    word = list(r.get_random_word())
    guesses = []
    guessed = list("_"*len(word)) 
    turns = math.floor((len(word)/2)+3) # or 6
    won = False

    while turns > 0:

        print(f"You have {turns} guesses left")

        print("".join(guessed))
        
        print(f"Your guessed letters: {','.join(guesses)}")


        guess = input("Enter guess: ")
        if((guess not in guesses)):
            guesses+=guess

        if(guess in word):
            for i in range(len(word)): 
                if (guess == word[i]):
                    guessed[i]= guess
        else:
            turns -= 1
            print("No dice")
        
        if (word==guessed):
            won=True
            break
    print(f"The word was {word}")        
    restart(won)

def restart(win_state):
    if(win_state):
        print("YOU'RE WINNER")
    else:
        print("NO WIN 4 U")
    choice = input("Wanna play again?: ")[0].lower()
    if (choice == "y"):
        print("OK, generating new game")
        new_game()
    else:
        print("Goodbye")
        

name = input("What is your name?: ")
print(f"Hi {name}, let's play some hangman!")
new_game()




        
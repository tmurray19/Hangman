import time
from random_word import RandomWords

#?
print ()
# Good, talk about printf
name = input("What's your name?" + "\n")
counts = 5
print ()
print ("Hello, " + name + ". I'm hangmaninator v1. Let's play hangman.")
print("Hello {}".format(name))
print(f"Hello {name} you have {counts} goes remaining")
# Sleep is odd, but i understand it
time.sleep(2)
r = RandomWords()
word = r.get_random_word()
print(word)
guesses = ''
turns = 10



name_of_var
NameOfVariable
nameOfVariable

# Love functions, let's talk about the conditions
def restart(cond):
    response = input("\n" + "You " + cond + ". Play again?")
    # Love the idea, but remember to be lazy af
    if response == "Y" or response =="y" or response =="yes" or response =="Yes":
        print("Great, let's see if you can get this one.")
    elif response == "N" or response == "n"or response =="no" or response =="No":
        print("\n" + "Ok, come again later.")
    else:
        print("\n" + "I don't understand, do you want to play again?")


while turns > 0:

    failed = 0

    guess = input ("\n" + "Guess a letter." + "\n")
    guesses += guess

    if guess not in word:
        turns -=1
        print ("\n" + "Wrong, you have", turns, "more guesses." "\n")

    if guess in word:
        print ("\n" + "Yep, that's in there." + "\n")
    
    print ("The word is:")
    
    for char in word:

        if char in guesses:
            print (char, end="")
        
        else:
            print ("_",end="")
            failed += 1

    if failed == 0:
        restart("win")


if turns == 0:
    restart("lose")


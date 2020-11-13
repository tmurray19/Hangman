import time
print ()
name = input("What's your name?" + "\n")
print ()
print ("Hello, " + name + ". I'm hangmaninator v1. Let's play hangman.")
time.sleep(2)
word = "serendipity"
guesses = ''
turns = 10

def restart(cond):
    response = input("\n" + "You " + cond + ". Play again?")
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
        print ("The word is:")

    if guess in word:
        print ("\n" + "Yep, that's in there." + "\n")
        print ("The word is:")
    
    for char in word:
        if char in guesses:
            print (char, end="")
        
        else:
            print ("_", end="")
            failed += 1

    if failed == 0:
        restart("win")


if turns == 0:
    restart("lose")


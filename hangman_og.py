import time

name = input("What's your name?")
print 
print ("Hello, " + name, " let's play hangman.")
time.sleep(1)
print ("guess a letter")
time.sleep(0.5)
word = "serendipity"
guesses = ''
turns = 10

while turns > 0:

    failed = 0
    
    for char in word:
        
        if char in guesses:
            print (char,)
        
        else:
            print ("_",)
            failed += 1
            break

    if failed == 0:
        print ("You win!",)
        break

print

guess = input ("guess a character")
guesses += guess

if guess not in word:
    turns -=1
    print ("Wrong")

print ("you have", + turns, "more guesses")

if turns == 0:
    print ("you lose")
#App 2: Guess the number 

#import 
import random


#Menu
#Inform the user what to do
print ("----------------")
print ("Guess the number")
print ("----------------")
print()

therandomnumber = random.randint(0, 100)

#Take the Input of the user
name = input("What is your name? ")
guess = -1

#Check input to see if they matched it successfully 

while guess != therandomnumber:
    guess_text = input("Guesss a number")
    guess = int(guess_text)

        if guess < therandomnumber:
            print ("Guess was too low")
        elif guess > therandomnumber:
             print ("Guess was too high")
        else:
            print("You got it right")

print ("Game over")
#if the guess is too low?
#if the guess is too high?
#if they guess correctly?

#display text

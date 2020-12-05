# App 2: Guess the number

# import
import random


# Menu
# Inform the user what to do
print("----------------")
print("Guess the number")
print("----------------")
print()

therandomnumber = random.randint(0, 10)

# Take the Input of the user
yourname = input("What is your name?: ")
guess = -1
numberofguesses = 0

# Check input to see if they matched it successfully

while guess != therandomnumber:
    guess_text = input("Guesss a number: ")
    guess = int(guess_text)
    numberofguesses = numberofguesses + 1
    if guess < therandomnumber:
        print("I'm sorry, {}, your guess was {} and it is too low. You have guessed {} times " .format( yourname, guess_text, numberofguesses))
    elif guess > therandomnumber:
        print("I'm sorry, {}, your guess was {} and it is too high. You have guessed {} times "  .format( yourname, guess_text, numberofguesses))
    else:
        print("You got it right!!!")

print("Game over.")
# if the guess is too low?
# if the guess is too high?
# if they guess correctly?

# display text

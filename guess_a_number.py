# guess a number

import random

top_of_range = int(input("Choose a number: "))

if top_of_range.isdigit ():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print ("Next time, choose number that is greater than 0.")
        quit ()

else:
    print("Choose a number the next time you try.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print ("Choose a number the next time you try.")
        continue

    if user_guess == random_number:
        print ("You did it")
        break
    elif user_guess > random_number:
        print ("Your guess is higher the number.")
    else:
        print ("Your guess is lower the number.")


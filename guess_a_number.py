# guess a number

import random

top_of_range = int(input("Choose a number: "))

if top_of_range.isdigit ():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print ("Next time, choose number that is greater than 0.")
        quit ()

else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue
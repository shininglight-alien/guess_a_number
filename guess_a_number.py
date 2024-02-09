# guess a number

import random

top_of_range = int(input("Choose a number: "))

if top_of_range.isdigit ():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print ("Next time, choose number that is greater than 0.")
        quit ()
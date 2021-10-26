import random

a=random.randint(1,9)

chances=0

while chances<6:
    b=int(input("Guess your number:"))
    if b==a:
        print("Correctly guessed!!!")
        break
    elif b>a:
        print("Guess too high")
        chances=chances+1
    elif b<a:
        print("Guess too low")
        chances=chances+1

if chances==0:
    print("You lose!!! Out of turns!!!")
    


import random
import time

minim = 1
maxim = 6

print("Welcome to the Roll The Dice Game!")

roll = True

while roll:
    print("""
  Do you want to play it?
    [y (Yes) / n (no)]\n""")
    roll = input("Choice: ").lower()
    if roll == 'y':
        print("\nRolling the dices...")
        time.sleep(1)
        print("The values are:", random.randint(minim, maxim), ",", random.randint(minim, maxim))
    elif roll == 'n':
        print("\nThank you for playing the game!")
        roll = False
    else:
        print("Invalid input")

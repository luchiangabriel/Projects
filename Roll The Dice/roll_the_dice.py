
import random

minim = 1
maxim = 6

print("""
Welcome to the Roll The Dice Game!
    Do you want to play it?
      [y (Yes) / n (no)]\n""")
roll = input("Choice: ")


while roll == "y":
    print("\nRolling the dices...")
    print("The values are:", random.randint(minim, maxim), ",", random.randint(minim, maxim))
    roll = input("\nRoll the dices again? [y (Yes) / n (no)]\nChoice: ").lower()

print("\nGood sesion of gaming!")

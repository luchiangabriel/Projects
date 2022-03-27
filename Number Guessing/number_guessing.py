
import random


def computer():
    i = list(range(1, 100))
    choice = random.choice(i)
    return choice


x = computer()

guess = 1

tries = 7
while guess != x:

    if guess in range(1, 100):
        print("\nTry to guess the number!")
        guess = int(input("Number: "))

    else:
        print("\nInvalid number!\nRange: 1 <-> 100")
        guess = int(input("Number: "))

    if tries == 0:
        print("\nOut of tries!\nAI Wins!\nMaybe next time!")
        break

    def hint():
        if x - 10 <= guess < x - 5 or x + 5 < guess <= x + 10:
            print("Warm!")
        elif x - 5 <= guess < x or x < guess <= x + 5:
            print("Hot!")
        elif x == guess:
            pass
        else:
            print("Cold!")

    hint()
    tries -= 1

else:

    print("""
|-----------|
| Found it! |
|-----------|""")

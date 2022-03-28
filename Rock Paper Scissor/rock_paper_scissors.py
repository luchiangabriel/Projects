
import random

active = True

print("Welcome to the Rock - Paper - Scissors Game!")

options = {
    1: 'Rock',
    2: 'Paper',
    3: 'Scissors'
    }

name = input("Enter your name: ").title()


def select():

    print("""
Please choose between: 1. Rock
                       2. Paper
                       3. Scissors""")

    choice = int(input("Enter: "))
    if choice in options.keys():
        choice = options.get(choice)
    else:
        print("Invalid input!")

    return choice


def computer():
    comp = random.randint(1, 3)
    return options.get(comp)


def rules(x, y):
    if x == y:
        print("Tie")
        game()
    elif x == "Rock" and x != y:
        if y == "Paper":
            return y
        elif y == "Scissors":
            return x
    elif x == "Paper" and x != y:
        if y == "Rock":
            return x
        elif y == "Scissors":
            return y
    elif x == "Scissors" and x != y:
        if y == "Rock":
            return y
        elif y == "Paper":
            return x


def game():
    global active

    while active:
        user = select()
        ai = computer()
        rules(user, ai)
        if rules(user, ai) == ai:
            print("AI wins!")
        else:
            print(f"{name} wins")

        def loop():
            global active
            print("\nWant to play again? [ y ( Yes ) / n ( No ) ]")
            again = input("Enter: ").lower()
            if again == 'y':
                game()
            elif again == 'n':
                print("\nThank you to playing the game!")
                exit()
            else:
                print("Invalid input")
        loop()


if __name__ == '__main__':
    game()

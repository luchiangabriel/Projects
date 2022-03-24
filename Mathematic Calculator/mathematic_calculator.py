
import math


class Calculator:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def gathering(self):
        result = self.first + self.second
        return result

    def substract(self):
        result = self.first - self.second
        return result

    def multiplication(self):
        result = self.first * self.second
        return result

    def division(self):
        if self.second == 0:
            raise ZeroDivisionError
        result = float(self.first / self.second)
        return result

    def rise_to_power(self):
        result = self.first ** self.second
        return result

    def radical(self):
        result = math.sqrt(self.first)
        return result


while True:

    def menu():
        x = ("""       
                Menu
        |--------------------|
        | 1. Gathering       |
        | 2. Down            |
        | 3. Multiplication  |
        | 4. Division        |
        | 5. Rise to power   |
        | 6. Radical         |
        | 0. Quit            |
        |____________________|""")
        print(x)

    menu()

    choice = int(input("Choose the option: "))

    if choice == 6:
        a = int(input("Number is: "))
        b = None
    elif choice < 0 or choice > 6:
        print("Invalid option")
        a = None
        b = None
    else:
        a = int(input("First number is: "))
        b = int(input("Second number is: "))

    operation = Calculator(a, b)

    if choice == 1:
        print("Result of gathering is: ", operation.gathering())
    elif choice == 2:
        print("Result of substract is: ", operation.substract())
    elif choice == 3:
        print("Result of multiplication is: ", operation.multiplication())
    elif choice == 4:
        print("Result of division is: ", operation.division())
    elif choice == 5:
        print("Result of rise to power is: ", operation.rise_to_power())
    elif choice == 6:
        print("Result of radical is: ", operation.radical())
    elif choice == 0:
        print("Quit the calculator!")
        break

    option = input("\nWant to do another calculation? [ y ( Yes ) / n ( No ) ]\nEnter: ").lower()
    if option == 'y':
        continue
    elif option == 'n':
        exit()

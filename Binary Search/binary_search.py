
import numpy as np


def binary_search1(bin_list, var):

    if var not in bin_list:
        print("The number is not in the list!")
        main()

    low = 0
    high = len(bin_list) - 1

    while low <= high:

        mid = (low + high) // 2

        if bin_list[mid] < var:
            low = mid + 1

        elif bin_list[mid] > var:
            high = mid - 1

        else:
            return mid

    return 0


def binary_search2(bin_list, var):

    if var not in bin_list:
        print("The number is not in the list!")
        main()

    low = 0
    high = len(bin_list) - 1
    ind = bin_list.index(var)

    while low <= high:

        mid = (low + high) // 2

        if bin_list.index(bin_list[mid]) < ind:
            low = mid + 1

        elif bin_list.index(bin_list[mid]) > ind:
            high = mid - 1

        else:
            return mid

    return 0


print("\n    Welcome to the binary search!")

again = """
              Menu              
    
    1. Binary search with a default list
    2. Binary search with a shuffled list
    0. Exit program\n"""


def main():
    option = True
    while option:

        print(again)
        option = int(input("Option: "))
        if option == 1:
            num_list = []

            for i in range(1, 101):
                num_list.append(i)
            print("List created!")

            x = int(input("Input the number: "))

            func = binary_search2(num_list, x)

            if func == 0:
                print("\nElement is not present in array!")
            else:
                print(f"\nElement {x} is present at index", str(func))

        elif option == 2:
            num_list = np.arange(1, 100)
            np.random.shuffle(num_list)
            num_list = list(num_list)
            print("List created!")

            x = int(input("Input the number: "))

            func = binary_search2(num_list, x)

            if func == 0:
                print("\nElement is not present in array!")
            else:
                print(f"\nElement {x} is present at index", str(func))

        elif option == 0:
            exit()

        print("\nTry again? [ y ( Yes ) / n ( No ) ]")
        ag = str(input("Enter: ")).lower()
        if ag == 'y':
            continue
        elif ag == 'n':
            option = 0


if __name__ == '__main__':
    main()

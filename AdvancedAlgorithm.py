# Sorting algorithm Menu
def sort_menu():
    while True:
        print("=======Sorting Menu=======")
        print("1: (Quick Sort Algorithm)")
        print("2: (Merge Sort Algorithm)")
        print("0: (Back to Main Menu)")

        user_input = int(input("-Enter Option:"))
        if user_input == 1:
            print("Quick Sort")
            continue
        elif user_input == 2:
            print("Merge Sort")
            continue
        elif user_input == 0:
            main_menu()
            break
        else:
            print("---Invalid Choose Between Options---")
            continue


# Searching Algorithm Menu
def searching_menu():
    while True:
        print("=======Searching Menu=======")
        print("1: (Linear Search)")
        print("2: (Binary Search)")
        print("0: (Back to Main Menu)")

        user_input = int(input("-Enter Option: "))
        if user_input == 1:
            print("Linear Searching")
            continue
        elif user_input == 2:
            print("Binary Searching")
            continue
        elif user_input == 0:
            main_menu()
            break
        else:
            print("---Invalid Choose Between Options---")
            continue


# Main Menu
def main_menu():
    while True:
        print("=======Choose from options=======")
        print("0: (Exit)")
        print("1: (Sorting algorithm)")
        print("2: (Searching algorithm)")

        # To catch an error for the input if its other than INT
        try:
            user_input = int(input("-Enter option: "))
        except ValueError:
            print("---Invalid input---")
            continue

        if user_input == 1:
            sort_menu()
            break
        elif user_input == 2:
            searching_menu()
            break
        elif user_input == 0:
            print("-Bye Bye-")
            break
        else:
            print("---Invalid Input---")
            continue


main_menu()

# Sorting algorithm Menus function (1)
def sort_menu():

    while True:
        print("=======Sorting Menu=======")
        print("1: (Quick Sort Algorithm)")
        print("2: (Merge Sort Algorithm)")
        print("0: (Back to Main Menu)")

        #Catches the error other than Int
        try:
            user_input = int(input("-Enter Option: "))
        except ValueError:
            print("---Invalid input---")
            continue
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


# Searching Algorithm Menu function (2)
def searching_menu():
    while True:
        print("=======Searching Menu=======")
        print("1: (Linear Search)")
        print("2: (Binary Search)")
        print("0: (Back to Main Menu)")

        try:
            user_input = int(input("-Enter Option: "))
        except ValueError:
            print("---Invalid input---")
            continue
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

# Quit program function 
def quit_program():
    print("Goodbye!")
    quit()


# Main Menu function 
def main_menu():
    while True:
        print("======MAIN=MENU=======")
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
            print("Sorting")
            sort_menu()
            break
        elif user_input == 2:
            searching_menu()
            break
        elif user_input == 0:
            quit_program()
        else:
            print("---Invalid Choose Between Options---")
            continue
main_menu()

#main_menu()#first function
#sort_menu() #second function 
#searching_menu() #third function 
#The menu seems to work iv tried to find bugs but it works fine i havent been able to connect the algortihms to he menu buttons main

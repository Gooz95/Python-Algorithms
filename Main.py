import random
from Algorithms import *


# class BluePrint for ending program 
class End(object):
    def __init__(self):
        pass
        
    def quit_program(self):
        print(40 * '=')
        print(15 * '-', "Goodbye!", 15 * '-')
        print(40 * '=')
        quit()
        
# Create an instance of the End class to use it later
end_object = End()


# Sort Menu class
class SortingMenu:
    @staticmethod


    # Display menu options
    def sorting_menu():
        while True:
            print(40 * '=')
            print(12 * '-', '[Sorting-Menu]', 12 * '-')
            print("1:--( Quick Sort Algorithm )", 11 * '-')
            print("2:--( Merge Sort Algorithm )", 11 * '-')
            print("0:--( Back to Main Menu )", 14 * '-')
            print(40 * '=')
            
            # Catch input errors
            try:
                user_input = int(input("-Enter Option: "))
            except ValueError:
                print("---Invalid input---")
                continue
            
            # Handle user input
            if user_input == 1:
                # Get user input for the array to be sorted
                while True:
                    input_str = input("Enter the elements(numbers only) of the array to be sorted, separated by spaces: ")
                    try:
                        array = [int(item) for item in input_str.split()]
                        break
                    except ValueError:
                        print("Please type numbers only.")
            
                # Sort the array using QuickSort
                sorted_array = Algorithms.quick_sort(array)
                
                # Print the sorted array
                print("Sorted array: ", sorted_array)
                continue
            
            
            elif user_input == 2:
                # Get user input for the array to be sorted
                while True:
                    input_str = input("Enter the elements of the array to be sorted, separated by spaces: ")
                    try:
                        array = [int(item) for item in input_str.split()]
                        break
                    except ValueError:
                        print("Please type numbers only.")
                # Sort the array using Merge Sort
                sorted_array = Algorithms.merge_sort(array)

                # Print the sorted array
                print("Sorted array: ", sorted_array)
                continue
            
            
            elif user_input == 0:
                MainMenu.display()  # Display the main menu
                break
            else:
                print("---Invalid Option Selected---")
                continue


# Searching Menu class
class SearchingMenu:
    @staticmethod
    
    
    # Display menu options
    def searching_menu():
        while True:
            print(40 * '=')
            print(11 * '-', '[Searching Menu]', 11 * '-')
            print("1:--( Linear Search )", 18 * '-')
            print("2:--( Binary Search )", 18 * '-')
            print("0:--( Back to Main Menu )", 14 * '-')
            print(40 * '=')

            # Catch input errors
            try:
                user_input = int(input("-Enter Option: "))
            except ValueError:
                print("---Invalid input---")
                continue
            
            # Handle user input
            if user_input == 1:
                array = [random.randint(0, 100) for n in range(10)]  # Random array (10 numbers) from 0 to 100
                print(f'This is a random list of 10 numbers between 0 and 100. \n{array}')  # print to the user
                target = int(input("Enter a target value: "))  # ask for target
                result = Algorithms.linear_search(array, target)  # using class obj > linear search 
                if result != -1:
                    print(40 * '=')
                    print(f"---Value {target} found at index {result}")  # if result found, print result
                    print(40 * '=')
                else:
                    print(40 * '=')
                    print(f"---{target} not found in list")  # otherwise print not found
                    print(40 * '=')
                    continue
            
            elif user_input == 2:
                array = [random.randint(0, 100) for n in range(10)]  # Random array (10 numbers) from 0 to 100
                sorted_array = Algorithms.quick_sort(array)  # sort the array to use binary search
                print(f'This is a random list of 10 numbers between 0 and 100. \n{sorted_array}')  # print to the user
                target = int(input("Enter a target value: "))  # ask for target
                result = Algorithms.binary_search(sorted_array, target)  # using class obj > binary search 
                
                if result != -1:
                    print(40 * '=')
                    print(f"---Value {target} found at index {result}")  # if result found, print result
                    print(40 * '=')
                else:
                    print(40 * '=')
                    print(f"---{target} not found in list")   # otherwise print not found
                    print(40 * '=')
                    continue
            
            
            elif user_input == 0:
                MainMenu.display()
                break
            else:
                print("---Invalid Choose Between Options---")
                continue


class MainMenu:
    @staticmethod
    def display():
        while True:
            print(40 * "=")
            print(10 * '-', "[ MAIN-MENU ]", 15 * '-')
            print("0:--( Exit )", 27 * '-')
            print("1:--( Sorting algorithm )", 14 * '-')
            print("2:--( Searching algorithm )", 12 * '-')
            print(40 * "=")

            # To catch an error for the input if it's other than INT
            try:
                user_input = int(input("-Enter option: "))
            except ValueError:
                print("---Invalid input---")
                continue

            if user_input == 1:
                print("Sorting")
                SortingMenu.sorting_menu()
                break
            elif user_input == 2:
                SearchingMenu.searching_menu()
                break
            elif user_input == 0:
                end_object.quit_program()
            else:
                print("---Invalid Choose Between Options---")
                continue

# block to ensure that it only runs when the script is executed directly. 
if __name__ == "__main__":
    MainMenu.display()

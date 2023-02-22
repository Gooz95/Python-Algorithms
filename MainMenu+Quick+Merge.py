class MergeSortMenu:
    def __init__(self):
        pass
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            mid = len(arr) // 2
            left = self.merge_sort(arr[:mid])
            right = self.merge_sort(arr[mid:])
            return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    def merge_menu(self):
        # Get user input for the array to be sorted
        while True:
            input_str = input("-Enter the elements of the array to be sorted, separated by spaces: ")
            try:
                arr = [int(x) for x in input_str.split()]
                break
            except ValueError:
                print("Please type numbers only.")

        # Sort the array using Merge Sort
        sorted_arr = self.merge_sort(arr)

        # Print the sorted array
        print("-Sorted --(Merge)-- array: ", sorted_arr)
merge_sorter = MergeSortMenu()

class QuickSortMenu:
    def __init__(self):
        pass
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less = [x for x in arr[1:] if x <= pivot]
            greater = [x for x in arr[1:] if x > pivot]
            return self.quick_sort(less) + [pivot] + self.quick_sort(greater)

    def quick_menu(self):
        # Get user input for the array to be sorted
        while True:
            input_str = input("-Enter the elements(numbers only) of the array to be sorted, separated by spaces: ")
            try:
                arr = [int(x) for x in input_str.split()]
                break
            except ValueError:
                print("Please type numbers only.")

        # Sort the array using QuickSort
        sorted_arr = self.quick_sort(arr)

        # Print the sorted array
        print("-Sorted ---(Quick)--- array: ", sorted_arr)
quick_sorter = QuickSortMenu()
###########################################################---Algortihms Above---##################################################

# class BP for ending program 
class End(object):
    def __init__(self):
        pass
        
    def quit_program(self):
        """
        A method to quit the program and display a goodbye message
        """
        print("Goodbye!")
        quit()

# Create an instance of the End class to use it later
end_object = End()
# obj created into a variable to be able to call within classes function from outside


# Sorting algorithm Menus function (1)
class SearchingMenu:
    def __init__(self):
        pass
    def searching_menu(self):
        while True:
            # Display menu options
            print("=======Searching Menu=======")
            print("1: (Linear Search)")
            print("2: (Binary Search)")
            print("0: (Back to Main Menu)")

            # Catch input errors
            try:
                user_input = int(input("-Enter Option: "))
            except ValueError:
                print("---Invalid input---")
                continue

            # Handle user input
            if user_input == 1:
                print("Linear Searching")
                continue
            elif user_input == 2:
                print("Binary Searching")
                continue
            elif user_input == 0:
                MainMenu.display()
                break
            else:
                print("---Invalid Choose Between Options---")
                continue
# Create instance of the searching menu class
search_menu_obj = SearchingMenu()


# Sort Menu class
class SortMenu:
    def __init__(self):
        # Constructor is empty because no additional initialization is needed
        pass
    
    # Method to display the sort menu
    def sort_menu(self):
        while True:
            print("======= Sorting Menu ========")
            print("1: Quick Sort Algorithm")
            print("2: Merge Sort Algorithm")
            print("0: Back to Main Menu")
            
            # Prompt user to enter an option and catch any invalid input
            try:
                user_input = int(input("-Enter Option: "))
            except ValueError:
                print("---Invalid input---")
                continue
            
            # Handle user input and perform corresponding action
            if user_input == 1:
                print("Quick Sort")
                quick_sorter.quick_menu()
                continue
            elif user_input == 2:
                print("Merge Sort")
                merge_sorter.merge_menu()
                continue 
            elif user_input == 0:
                MainMenu.display()  # Display the main menu
                break
            else:
                print("---Invalid Option Selected---")
                continue
# Create an instance of the SortMenu class
sort_menu_obj = SortMenu()

class MainMenu:
    @staticmethod
    def display():
        while True:
            print("======MAIN=MENU=======")
            print("0: (Exit)")
            print("1: (Sorting algorithm)")
            print("2: (Searching algorithm)")

            # To catch an error for the input if it's other than INT
            try:
                user_input = int(input("-Enter option: "))
            except ValueError:
                print("---Invalid input---")
                continue

            if user_input == 1:
                print("Sorting")
                sort_menu_obj.sort_menu()
                break
            elif user_input == 2:
                search_menu_obj.searching_menu()
                break
            elif user_input == 0:
                end_object.quit_program()
            else:
                print("---Invalid Choose Between Options---")
                continue

# block to ensure that it only runs when the script is executed directly. 
if __name__ == "__main__":
    MainMenu.display()

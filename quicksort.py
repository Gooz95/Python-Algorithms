
# Defining funtion quick sort algorithm
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [item for item in array[1:] if item <= pivot]
        greater = [item for item in array[1:] if item > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Get user input for the array to be sorted
while True:
    input_str = input("Enter the elements(numbers only) of the array to be sorted, separated by spaces: ")
    try:
        array = [int(item) for item in input_str.split()]
        break
    except ValueError:
        print("Please type numbers only.")

# Sort the array using QuickSort
sorted_array = quick_sort(array)

# Print the sorted array
print("Sorted array: ", sorted_array)


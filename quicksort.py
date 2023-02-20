def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Get user input for the array to be sorted
while True:
    input_str = input("Enter the elements(numbers only) of the array to be sorted, separated by spaces: ")
    try:
        arr = [int(x) for x in input_str.split()]
        break
    except ValueError:
        print("Please type numbers only.")

# Sort the array using QuickSort
sorted_arr = quick_sort(arr)

# Print the sorted array
print("Sorted array: ", sorted_arr)


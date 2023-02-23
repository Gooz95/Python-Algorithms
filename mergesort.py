
# Defining function for merge sort algorithm
def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        return merge(left, right)

def merge(left, right):
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

# Get user input for the array to be sorted
while True:
    input_str = input("Enter the elements of the array to be sorted, separated by spaces: ")
    try:
        array = [int(item) for item in input_str.split()]
        break
    except ValueError:
        print("Please type numbers only.")

# Sort the array using Merge Sort
sorted_array = merge_sort(array)

# Print the sorted array
print("Sorted array: ", sorted_array)

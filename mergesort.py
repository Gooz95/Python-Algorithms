def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
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
        arr = [int(x) for x in input_str.split()]
        break
    except ValueError:
        print("Please type numbers only.")

# Sort the array using Merge Sort
sorted_arr = merge_sort(arr)

# Print the sorted array
print("Sorted array: ", sorted_arr)

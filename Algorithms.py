class Algorithms:  # Defining Class Algorithms
    @staticmethod # Static method to be able to call the functions whitout class object
    
    
    def quick_sort(array):  # static method implementing quicksort algorithm
        if len(array) <= 1:  # base case: return the array if it has length 0 or 1
            return array
        else:
            pivot = array[0]  # choose first element as pivot
            print(f'This is the pivot: {pivot}')
            less = [item for item in array[1:] if item <= pivot]  # create two subarrays: one with elements <= pivot, the other with elements > pivot
            print(f'This is the variable "less or equal than pivot {pivot}": {less}')
            greater = [item for item in array[1:] if item > pivot]
            print(f'This is the varible "greater than pivot {pivot}": {greater if greater else "None"}')
            return Algorithms.quick_sort(less) + [pivot] + Algorithms.quick_sort(greater)  # recursively call quick_sort on the subarrays, and concatenate the sorted subarrays with the pivot
    
    
    def merge_sort(array):
        print("Splitting", array)
        # Check if the length of the array is greater than 1
        if len(array) > 1:
            # Divide the array into two halves
            mid = len(array) // 2
            left_arr = array[:mid]
            right_arr = array[mid:]
            
            # Recursive call to divide left and right halves
            Algorithms.merge_sort(left_arr)
            Algorithms.merge_sort(right_arr)
            
            # Merge sorted halves
            left_index = right_index = 0
            merged_arr = []
            while left_index < len(left_arr) and right_index < len(right_arr):
                # If element in the left half is smaller, add it to the merged array
                if left_arr[left_index] < right_arr[right_index]:
                    merged_arr.append(left_arr[left_index])
                    left_index += 1
                # If element in the right half is smaller, add it to the merged array
                else:
                    merged_arr.append(right_arr[right_index])
                    right_index += 1
                # Print information about selecting and adding smaller numbers to merged array
                print("Selected smaller element from", "left subarray" if left_arr[left_index-1] < right_arr[right_index-1] else "right subarray", ":", merged_arr[-1])
            
            # If there are any remaining elements in the left half, add them to the merged array
            while left_index < len(left_arr):
                merged_arr.append(left_arr[left_index])
                left_index += 1
                # Print information about adding remaining elements from left subarray to merged array
                print("Added remaining element from left subarray to merged array:", merged_arr[-1])
            
            # If there are any remaining elements in the right half, add them to the merged array
            while right_index < len(right_arr):
                merged_arr.append(right_arr[right_index])
                right_index += 1
                # Print information about adding remaining elements from right subarray to merged array
                print("Added remaining element from right subarray to merged array:", merged_arr[-1])
            
            # Copy merged array back to original array
            for i in range(len(merged_arr)):
                array[i] = merged_arr[i]
            
            # Print information about the merge step
            print("Merging", left_arr, "and", right_arr)
        return array
    
    
    def binary_search(array, target):  # Defining the binary search function
        left, right = 0, len(array) - 1  # Starting variables and end indice
        
        while left <= right:  # Loop until left is greater
            mid = (left + right) // 2  # pick the middle
            print(f"Left: {left}, Right: {right}, Mid: {mid}")
            if array[mid] == target:  # if the middle is the target return its index
                print(f"Found target {target} at index {mid}")
                return mid
            elif array[mid] < target:  # If the middle element is less than the target, search in the right half of the array
                left = mid + 1
                print(f"Target {target} is in right half of array")
            else:
                right = mid - 1   # if is greater then search in the left
                print(f"Target {target} is in left half of array")
        print(f"Target {target} not found in array")
        return -1   # if not found return -1
    
    
    def linear_search(array, target):  # Defining the linear search function
        for item in range(len(array)):  # Loop through each element in the array
            if array[item] == target:  # If the current element is equal to the target value, return its index
                return item
        return -1 # If the target value is not found in the array, return -1, at the end print message

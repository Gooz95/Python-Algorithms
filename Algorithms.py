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


    def merge_sort(array):  # static method implementing mergesort algorithm
        if len(array) <= 1: # base case: return the array if it has length 0 or 1
            return array
        else:
            mid = len(array) // 2  # find midpoint of array
            # print(F'This is the index position of mid point of the array = {mid}')
            left = Algorithms.merge_sort(array[:mid])  # recursively call merge_sort on the left and right halves of the array
            # print(f'left')
            right = Algorithms.merge_sort(array[mid:])
            print(f'This is the left array:{left}. This is the right array:{right}.')
            print(f'The array is: {array}')
            
            return Algorithms.merge(left, right)  # call merge method to merge the sorted left and right subarrays

    def merge(left, right):  # static method implementing merge operation to merge two sorted arrays
        result = []
        i, j = 0, 0
        print(left)
        print(right)
        while i < len(left) and j < len(right):  # loop through the left and right arrays and compare elements
            # print(i)
            # print(j)
            if left[i] <= right[j]:
                
                result.append(left[i])
                i += 1
                print(f'This is the result up to now. {result}')
                # print(i)
            else:
                result.append(right[j])
                j += 1
                # print(result)
                # print(j)
        
        # add any remaining elements from either array to the result array
        result += left[i:]
        # print(result)
        result += right[j:]
        # print(result)
        return result


    def binary_search(array, target):  # Defining the binary search function
        left, right = 0, len(array) - 1  # Starting variables and end indice
        
        while left <= right:  # Loop until left is greater
            mid = (left + right) // 2  # pick the middle
            if array[mid] == target:  # if the middle is the target return its index
                return mid
            elif array[mid] < target:  # If the middle element is less than the target, search in the right half of the array
                left = mid + 1
            else:
                right = mid - 1   # if is greater then search in the left
        return -1   # if not found return -1

    def linear_search(array, target):  # Defining the linear search function
        for item in range(len(array)):  # Loop through each element in the array
            if array[item] == target:  # If the current element is equal to the target value, return its index
                return item
        return -1 # If the target value is not found in the array, return -1, at the end print message

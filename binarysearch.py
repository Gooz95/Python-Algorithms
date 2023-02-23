class BinarySearch:
    @staticmethod
    
    # Defining the binary search function
    def binary_search(array, target):
        # Starting variables and end indice
        left, right = 0, len(array) - 1
        
        # Loop until left is greater
        while left <= right:
            mid = (left + right) // 2  # pick the middle
            if array[mid] == target:  # if the middle is the target return its index
                return mid
            elif array[mid] < target:  # If the middle element is less than the target, search in the right half of the array
                left = mid + 1
            else:
                right = mid - 1   # if is greater then search in the left
        return -1   # if not found return -1

class LinearSearch:
    @staticmethod
    
    # Defining the linear search function
    def linear_search(array, target):
        # Loop through each element in the array
        for item in range(len(array)):
            # If the current element is equal to the target value, return its index
            if array[item] == target:
                return item
        # If the target value is not found in the array, return -1, at the end print message
        return -1

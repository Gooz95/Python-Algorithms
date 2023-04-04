# Import necessary libraries
import csv
import random
from math import log2
from collections import Counter


def entropy(data):      # Define a function to calculate the entropy of a dataset
    counts = Counter(row[-1] for row in data)   # Count the number of occurrences of each class in the dataset
    total = sum(counts.values())    # Calculate the total number of rows in the dataset
    return -sum(count / total * log2(count / total) for count in counts.values())    # Calculate and return the entropy of the dataset


def information_gain(data, column_index):    # Define a function to calculate the information gain of a column in a dataset
    total_entropy = entropy(data)       # Calculate the entropy of the entire dataset
    split_entropy = 0           # Initialize a variable to store the split entropy
    for value in set(row[column_index] for row in data):        # Iterate over each unique value in the column
        subset = [row for row in data if row[column_index] == value]    # Create a subset of the data where the column has the current value
        split_entropy += len(subset) / len(data) * entropy(subset)  # Calculate the weighted entropy of the subset and add it to the split entropy
    return total_entropy - split_entropy     # Return the information gain of splitting on this column


def best_split(data):   # Define a function to find the best column to split the dataset on
    best_column_index = None        # Initialize variables to store the best column index and information gain
    best_information_gain = 0
    for column_index in range(len(data[0]) - 1):    # Iterate over each column index (except for the last one, which is the class column)
        ig = information_gain(data, column_index)     # Calculate the information gain of splitting on this column
        if ig > best_information_gain:         # If this information gain is better than the current best, update the best values
            best_column_index = column_index
            best_information_gain = ig
    return best_column_index      # Return the index of the best column to split on


def build_tree(data):   # Define a recursive function to build a decision tree from a dataset
    if len(set(row[-1] for row in data)) == 1:    # If all rows have the same class, return that class as a leaf node
        return data[0][-1]

    column_index = best_split(data)    # Find the best column to split on using information gain
    tree = {}    # Initialize an empty dictionary to store the tree structure
    for value in set(row[column_index] for row in data):    # Iterate over each unique value in the best column to split on
        subset = [row for row in data if row[column_index] == value]     # Create a subset of the data where the best column has this value
        tree[value] = build_tree(subset)     # Recursively build a subtree using this subset and add it to the tree structure under this value key
    return (column_index, tree)    # Return a tuple containing the index of the best column to split on and its tree structure as a dictionary


def predict(tree, row):     # Define a function to make a prediction using a decision tree and an input row
    if not isinstance(tree, tuple):    # If we have reached a leaf node (i.e. not a tuple), return its value as our prediction
        return tree
    column_index, subtree = tree     # Unpack our tree tuple into its two components: index of splitting column and subtree structure as dictionary 
    value = row[column_index]    # Get value from input row at splitting column index 
    
    if value not in subtree:    # If input value is not present in subtree keys then return None 
        return None
    
    return predict(subtree[value], row)    # Recursively call predict function with subtree at input value key and input row 


def bootstrap_sample(data):     # Define a function to create a bootstrap sample from a dataset
    sample = []    # Initialize an empty list to store the bootstrap sample
    n = len(data)    # Get the number of rows in the dataset
    for _ in range(n):    # Iterate over the number of rows in the dataset
        index = random.randrange(n)    # Generate a random index between 0 and n-1
        sample.append(data[index])     # Append the row at the generated index to the bootstrap sample
    return sample    # Return the bootstrap sample


def build_random_forest(data, n_trees):     # Define a function to build a random forest from a dataset and number of trees
    forest = []    # Initialize an empty list to store the forest (i.e. list of trees)
    for _ in range(n_trees):    # Iterate over the number of trees specified
        sample = bootstrap_sample(data)        # Create a bootstrap sample from the dataset
        tree = build_tree(sample)        # Build a decision tree using the bootstrap sample
        forest.append(tree)        # Append the tree to the forest
    return forest    # Return the forest (i.e. list of trees)


def predict_random_forest(forest, row):     # Define a function to make a prediction using a random forest and an input row
    predictions = [predict(tree, row) for tree in forest]    # Make a prediction using each tree in the forest
    return max(set(predictions), key=predictions.count)    # Return the most common prediction among all trees


with open('covid_symptoms.csv', newline='') as f:   # Load the data from a CSV file
    reader = csv.reader(f)    # Create a CSV reader object
    header = next(reader)    # Read and store the header row
    data = []    # Initialize an empty list to store the data
    for row in reader:    # Iterate over each row in the CSV file
        data.append([int(value) for value in row])   # Convert each value in the row to an integer and append it to the data list


random.shuffle(data)                 # Shuffle the data randomly
split_point = int(len(data) * 0.8)   # Calculate the split point as 80% of the number of rows in the dataset
train_data = data[:split_point]      # Split the data into training and test sets using the calculated split point
test_data = data[split_point:]


n_trees = 100       # Build a random forest using the training data
forest = build_random_forest(train_data, n_trees)


symptoms = []   # Accept user input for symptoms and validate the input
for symptom in header[:-1]:
    while True:
        response = input(f'Do you have {symptom}? (yes/no) ').lower()
        if response in {'yes', 'y'}:
            symptoms.append(1)
            break
        elif response in {'no', 'n'}:
            symptoms.append(0)
            break
        else:
            print('Invalid input. Please enter yes or no.')


prediction = predict_random_forest(forest, symptoms)    # Make a prediction based on the user's input symptoms
print(f'Prediction: {prediction}')


if prediction == 1:     # Print a message to the user based on the prediction
    print(f'According to the random forest model with {n_trees} trees, you are more likely to have COVID-19.')
else:
    print(f'According to the random forest model with {n_trees} trees, you are less likely to have COVID-19.')

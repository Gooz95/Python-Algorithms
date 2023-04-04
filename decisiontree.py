# import pandas as pd
# import numpy as np
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score

# # load the dataset
# data = pd.read_csv('covid_dataset.csv')

# # split the data into inputs (X) and outputs (y)
# X = data.iloc[:, :-1]
# y = data.iloc[:, -1]

# # create a dictionary to map user input to binary values
# symptoms_map = {'yes': 1, 'no': 0}

# # define a function to get user input and validate it
# def get_input(symptom):
#     while True:
#         user_input = input(f"Do you have {symptom}? (yes/no) ").lower()
#         if user_input in symptoms_map:
#             return symptoms_map[user_input]
#         print("Invalid input, please try again.")

# # get user input for each symptom
# fever = get_input("fever")
# cough = get_input("cough")
# fatigue = get_input("fatigue")
# breathlessness = get_input("breathlessness")
# headache = get_input("headache")

# # create a numpy array with the user input
# user_input = np.array([fever, cough, fatigue, breathlessness, headache]).reshape(1, -1)

# # train the model and make a prediction
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X, y)
# prediction = model.predict(user_input)

# # print the prediction
# if prediction == 1:
#     print("You are more likely to have COVID-19.")
# else:
#     print("You are less likely to have COVID-19.")



# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier

# # Load the data from a CSV file
# data = pd.read_csv('covid_symptoms.csv')

# # Split the data into training and test sets
# X = data.drop('covid_positive', axis=1)
# y = data['covid_positive']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# # Create and train the decision tree classifier
# clf = DecisionTreeClassifier()
# clf.fit(X_train, y_train)

# # Make predictions on the test set
# y_pred = clf.predict(X_test)

# # Evaluate the model's performance
# accuracy = (y_pred == y_test).mean()
# print(f'Accuracy: {accuracy:.2f}')

# # Load the data from a CSV file
# import csv
# with open('covid_symptoms.csv', newline='') as f:
#     reader = csv.reader(f)
#     data = list(reader)

# # Split the data into training and test sets
# import random
# random.shuffle(data)
# split_point = int(len(data) * 0.8)
# train_data = data[:split_point]
# test_data = data[split_point:]

# # Define a function to calculate the entropy of a dataset
# def entropy(data):
#     from collections import Counter
#     from math import log2
#     counts = Counter(row[-1] for row in data)
#     total = sum(counts.values())
#     return -sum(count / total * log2(count / total) for count in counts.values())

# # Define a function to calculate the information gain of a split
# def information_gain(data, column_index):
#     total_entropy = entropy(data)
#     split_entropy = 0
#     for value in set(row[column_index] for row in data):
#         subset = [row for row in data if row[column_index] == value]
#         split_entropy += len(subset) / len(data) * entropy(subset)
#     return total_entropy - split_entropy

# # Define a function to find the best split for a dataset
# def best_split(data):
#     best_column_index = None
#     best_information_gain = 0
#     for column_index in range(len(data[0]) - 1):
#         ig = information_gain(data, column_index)
#         if ig > best_information_gain:
#             best_column_index = column_index
#             best_information_gain = ig
#     return best_column_index

# # Define a function to build a decision tree
# def build_tree(data):
#     if len(set(row[-1] for row in data)) == 1:
#         return data[0][-1]
#     column_index = best_split(data)
#     tree = {}
#     for value in set(row[column_index] for row in data):
#         subset = [row for row in data if row[column_index] == value]
#         tree[value] = build_tree(subset)
#     return (column_index, tree)

# # Build the decision tree using the training data
# tree = build_tree(train_data)

# # Define a function to make predictions using the decision tree
# def predict(tree, row):
#     if not isinstance(tree, tuple):
#         return tree
#     column_index, subtree = tree
#     value = row[column_index]
#     if value not in subtree:
#         return None
#     return predict(subtree[value], row)

# # Make predictions on the test set and evaluate the model's performance
# correct_predictions = 0
# for row in test_data:
#     prediction = predict(tree, row)
#     if prediction == row[-1]:
#         correct_predictions += 1

# accuracy = correct_predictions / len(test_data)
# print(f'Accuracy: {accuracy:.2f}')


# Load the data from a CSV file
import random
import csv

with open('covid_symptoms.csv', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = []
    for row in reader:
        data.append([int(value) for value in row])

# Split the data into training and test sets
random.shuffle(data)
split_point = int(len(data) * 0.8)
train_data = data[:split_point]
test_data = data[split_point:]

# Define a function to calculate the entropy of a dataset
def entropy(data):
    from collections import Counter
    from math import log2
    counts = Counter(row[-1] for row in data)
    total = sum(counts.values())
    return -sum(count / total * log2(count / total) for count in counts.values())

# Define a function to calculate the information gain of a split
def information_gain(data, column_index):
    total_entropy = entropy(data)
    split_entropy = 0
    for value in set(row[column_index] for row in data):
        subset = [row for row in data if row[column_index] == value]
        split_entropy += len(subset) / len(data) * entropy(subset)
    return total_entropy - split_entropy

# Define a function to find the best split for a dataset
def best_split(data):
    best_column_index = None
    best_information_gain = 0
    for column_index in range(len(data[0]) - 1):
        ig = information_gain(data, column_index)
        if ig > best_information_gain:
            best_column_index = column_index
            best_information_gain = ig
    return best_column_index

# Define a function to build a decision tree
def build_tree(data):
    if len(set(row[-1] for row in data)) == 1:
        return data[0][-1]
    column_index = best_split(data)
    tree = {}
    for value in set(row[column_index] for row in data):
        subset = [row for row in data if row[column_index] == value]
        tree[value] = build_tree(subset)
    return (column_index, tree)

# Build the decision tree using the training data
tree = build_tree(train_data)

# Define a function to make predictions using the decision tree
def predict(tree, row):
    if not isinstance(tree, tuple):
        return tree
    column_index, subtree = tree
    value = row[column_index]
    if value not in subtree:
        return None
    return predict(subtree[value], row)

"""BOOTSTRAP IS A BOOSTER TO MAKE THE DECISION TREE MORE ACCURATE, THE DECISION TREE WORKS ON HIS OWN BUT WITH THE BOOTSRAP HAS MORE ACCURRANCY ON THE PREDICTION"""
"""BY USING THE DECISION TREE WITH THE BOOTSTRAP THE ALGORITHM BECOME THE RANDOM FOREST ALGORITHM INSTEAD OF DECISION TREE"""
# Define a function to bootstrap a dataset
def bootstrap(data):
    return [random.choice(data) for _ in range(len(data))]

# Define a function to make predictions using an ensemble of decision trees
def predict_ensemble(trees, row):
    predictions = [predict(tree, row) for tree in trees]
    return max(set(predictions), key=predictions.count)

# Generate synthetic data using bootstrapping and train an ensemble of decision trees
n_trees = 10
trees = []
for _ in range(n_trees):
    bootstrapped_data = bootstrap(data)
    tree = build_tree(bootstrapped_data)
    trees.append(tree)
"""BOOTSRAP ENDS HERE"""

# Accept user input for symptoms and validate the input
symptoms = []
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

# Make a prediction based on the user's input symptoms
# prediction = predict(tree, symptoms)    # prediction using only the decision tree
prediction = predict_ensemble(trees, symptoms)     # prediction using the bootstrap
print(f'Prediction: {prediction}')

# Print a message to the user based on the prediction
if prediction == 1:
    print('According to the decision tree, you are more likely to have COVID-19.')
else:
    print('According to the decision tree, you are less likely to have COVID-19.')
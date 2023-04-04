import csv
import random
from math import log2

def entropy(data):
    from collections import Counter
    counts = Counter(row[-1] for row in data)
    total = sum(counts.values())
    return -sum(count / total * log2(count / total) for count in counts.values())

def information_gain(data, column_index):
    total_entropy = entropy(data)
    split_entropy = 0
    for value in set(row[column_index] for row in data):
        subset = [row for row in data if row[column_index] == value]
        split_entropy += len(subset) / len(data) * entropy(subset)
    return total_entropy - split_entropy

def best_split(data):
    best_column_index = None
    best_information_gain = 0
    for column_index in range(len(data[0]) - 1):
        ig = information_gain(data, column_index)
        if ig > best_information_gain:
            best_column_index = column_index
            best_information_gain = ig
    return best_column_index

def build_tree(data):
    if len(set(row[-1] for row in data)) == 1:
        return data[0][-1]
    column_index = best_split(data)
    tree = {}
    for value in set(row[column_index] for row in data):
        subset = [row for row in data if row[column_index] == value]
        tree[value] = build_tree(subset)
    return (column_index, tree)

def predict(tree, row):
    if not isinstance(tree, tuple):
        return tree
    column_index, subtree = tree
    value = row[column_index]
    if value not in subtree:
        return None
    return predict(subtree[value], row)

def bootstrap_sample(data):
    sample = []
    n = len(data)
    for _ in range(n):
        index = random.randrange(n)
        sample.append(data[index])
    return sample

def build_random_forest(data, n_trees):
    forest = []
    for _ in range(n_trees):
        sample = bootstrap_sample(data)
        tree = build_tree(sample)
        forest.append(tree)
    return forest

def predict_random_forest(forest, row):
    predictions = [predict(tree, row) for tree in forest]
    return max(set(predictions), key=predictions.count)

# Load the data from a CSV file
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

# Build a random forest using the training data
n_trees = 100
forest = build_random_forest(train_data, n_trees)

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
prediction = predict_random_forest(forest, symptoms)
print(f'Prediction: {prediction}')

# Print a message to the user based on the prediction
if prediction == 1:
    print(f'According to the random forest model with {n_trees} trees, you are more likely to have COVID-19.')
else:
    print(f'According to the random forest model with {n_trees} trees, you are less likely to have COVID-19.')
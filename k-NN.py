import csv
import random
from math import sqrt

def euclidean_distance(row1, row2):
    return sqrt(sum([(a - b) ** 2 for a, b in zip(row1, row2)]))

def get_neighbors(X_train, y_train, x_test, k):
    distances = []
    for x, y in zip(X_train, y_train):
        d = euclidean_distance(x, x_test)
        distances.append((x, y, d))
    distances.sort(key=lambda x: x[2])
    return [y for _, y, _ in distances[:k]]

def predict(X_train, y_train, x_test, k):
    neighbors = get_neighbors(X_train, y_train, x_test, k)
    return max(set(neighbors), key=neighbors.count)

# Load the data from a CSV file
with open('covid_dataset.csv', newline='') as f:
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

# Separate the features and the target variable
X_train = [row[:-1] for row in train_data]
y_train = [row[-1] for row in train_data]
X_test = [row[:-1] for row in test_data]
y_test = [row[-1] for row in test_data]

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
k = 10
prediction = predict(X_train, y_train, symptoms, k)
print(f'Prediction: {prediction}')

# Print a message to the user based on the prediction
if prediction == 1:
    print(f'According to the k-NN model with k={k}, you are more likely to have COVID-19.')
else:
    print(f'According to the k-NN model with k={k}, you are less likely to have COVID-19.')
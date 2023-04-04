import csv
import random
from math import exp

def dot_product(v1, v2):
    return sum([x * y for x, y in zip(v1, v2)])

def predict(X_train, y_train, x_test, coefficients, bias):
    result = bias
    for x_i, y_i in zip(X_train, y_train):
        result += dot_product(coefficients[y_i], x_i)
    return 1 if result > 0 else 0

def train_svm(X_train, y_train, learning_rate=0.1, num_iterations=1000):
    n_classes = len(set(y_train))
    n_features = len(X_train[0])
    coefficients = [[0] * n_features for _ in range(n_classes)]
    bias = 0
    for _ in range(num_iterations):
        for x_i, y_i in zip(X_train, y_train):
            if (y_i * (dot_product(coefficients[y_i], x_i) + bias)) < 1:
                coefficients[y_i] = [c + learning_rate * (y_i * x - 2 * (1 / num_iterations) * c) for c, x in zip(coefficients[y_i], x_i)]
                bias += learning_rate * y_i
            else:
                coefficients[y_i] = [c + learning_rate * (-2 * (1 / num_iterations) * c) for c in coefficients[y_i]]
    return coefficients, bias

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

# Separate the features and the target variable
X_train = [row[:-1] for row in train_data]
y_train = [row[-1] for row in train_data]
X_test = [row[:-1] for row in test_data]
y_test = [row[-1] for row in test_data]

# Train an SVM model
coefficients, bias = train_svm(X_train, y_train)

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
prediction = predict(X_train, y_train, symptoms, coefficients, bias)
print(f'Prediction: {prediction}')

# Print a message to the user based on the prediction
if prediction == 1:
    print('According to the SVM model, you are more likely to have COVID-19.')
else:
    print('According to the SVM model, you are less likely to have COVID-19.')

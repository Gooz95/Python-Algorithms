import csv
import random
import math


def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def predict_probabilities(X, coefficients):
    return [sigmoid(sum([x * c for x, c in zip(row, coefficients)])) for row in X]

def predict(X, coefficients):
    probabilities = predict_probabilities(X, coefficients)
    return [1 if p > 0.5 else 0 for p in probabilities]

def cost_function(X, y, coefficients):
    probabilities = predict_probabilities(X, coefficients)
    return -sum([y_i * math.log(p) + (1 - y_i) * math.log(1 - p) for y_i, p in zip(y, probabilities)])

def gradient_descent(X, y, coefficients, learning_rate):
    new_coefficients = []
    probabilities = predict_probabilities(X, coefficients)
    for j in range(len(coefficients)):
        gradient = sum([(p - y_i) * X[i][j] for i, (y_i, p) in enumerate(zip(y, probabilities))])
        new_coefficients.append(coefficients[j] - learning_rate * gradient)
    return new_coefficients

def logistic_regression(X_train, y_train, learning_rate=0.1, num_iterations=1000):
    coefficients = [0] * len(X_train[0])
    for _ in range(num_iterations):
        coefficients = gradient_descent(X_train, y_train, coefficients, learning_rate)
    return coefficients

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

# Train a logistic regression model
coefficients = logistic_regression(X_train, y_train)

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
prediction = predict([symptoms], coefficients)[0]
print(f'Prediction: {prediction}')

# Print a message to the user based on the prediction
if prediction == 1:
    print('According to the logistic regression model, you are more likely to have COVID-19.')
else:
    print('According to the logistic regression model, you are less likely to have COVID-19.')

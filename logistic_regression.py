# Import necessary libraries
import csv # for reading data from a CSV file
import random # for shuffling the data before splitting into training and test sets
import math # for mathematical operations such as exponential and logarithmic functions


def sigmoid(z):     # Define the sigmoid function, which is used to map any real-valued number to a value between 0 and 1
    return 1 / (1 + math.exp(-z))


# Define a function to predict probabilities using the logistic regression model
# This function takes in a matrix of features (X) and a vector of coefficients (coefficients)
# It returns a vector of predicted probabilities for each row in X
def predict_probabilities(X, coefficients):
    # For each row in X, calculate the dot product between the row and the coefficients vector
    # Then apply the sigmoid function to the result to get the predicted probability
    return [sigmoid(sum([x * c for x, c in zip(row, coefficients)])) for row in X]


# Define a function to make predictions using the logistic regression model
# This function takes in a matrix of features (X) and a vector of coefficients (coefficients)
# It returns a vector of predicted binary outcomes (0 or 1) for each row in X
def predict(X, coefficients):
    probabilities = predict_probabilities(X, coefficients)    # First, use the predict_probabilities function to get the predicted probabilities for each row in X
    return [1 if p > 0.5 else 0 for p in probabilities]    # Then, for each probability, return 1 if it is greater than 0.5 and 0 otherwise


# Define the cost function for logistic regression
# This function takes in a matrix of features (X), a vector of true binary outcomes (y), and a vector of coefficients (coefficients)
# It returns the value of the cost function for the given data and coefficients
def cost_function(X, y, coefficients):
    probabilities = predict_probabilities(X, coefficients)    # First, use the predict_probabilities function to get the predicted probabilities for each row in X
    return -sum([y_i * math.log(p) + (1 - y_i) * math.log(1 - p) for y_i, p in zip(y, probabilities)])    # Then, calculate the value of the cost function using the formula for binary cross-entropy loss


# Define a function to perform gradient descent to update the coefficients of the logistic regression model
# This function takes in a matrix of features (X), a vector of true binary outcomes (y), a vector of current coefficients (coefficients), and a learning rate (learning_rate)
# It returns an updated vector of coefficients after performing one step of gradient descent
def gradient_descent(X, y, coefficients, learning_rate):
    new_coefficients = []
    probabilities = predict_probabilities(X, coefficients)    # First, use the predict_probabilities function to get the predicted probabilities for each row in X
    for j in range(len(coefficients)):    # Then, for each coefficient:
        gradient = sum([(p - y_i) * X[i][j] for i, (y_i, p) in enumerate(zip(y, probabilities))])   # Calculate the gradient of the cost function with respect to that coefficient using partial derivatives
        new_coefficients.append(coefficients[j] - learning_rate * gradient)     # Update the coefficient by subtracting the product of the learning rate and the gradient from its current value
    return new_coefficients   # return the new coefficients


# Define a function to train a logistic regression model using gradient descent
# This function takes in a matrix of training features (X_train), a vector of training binary outcomes (y_train), a learning rate (learning_rate), and a number of iterations (num_iterations)
# It returns a trained vector of coefficients after performing gradient descent for num_iterations steps
def logistic_regression(X_train, y_train, learning_rate=0.1, num_iterations=1000):
    coefficients = [0] * len(X_train[0])    # Initialize all coefficients to 0
    for _ in range(num_iterations):    # Perform gradient descent for num_iterations steps:
        coefficients = gradient_descent(X_train, y_train, coefficients, learning_rate)   # Use the gradient_descent function to update the coefficients after each step
    return coefficients   # return the coefficients


with open('covid_dataset.csv', newline='') as f:    # Load data from 'covid_dataset.csv' file into 'data' list.
    reader = csv.reader(f)     # Create a CSV reader object
    header = next(reader)   # Read header row containing column names
    data = []   # Initialize an empty list to store the data
    for row in reader:    # Iterate over each row in the CSV file
        data.append([int(value) for value in row])    # Convert each value in the row to an integer and append the row to the data list


random.shuffle(data)    # Shuffle the data randomly
split_point = int(len(data) * 0.8)    # Calculate the split point for dividing the data into training and test sets (80% training, 20% test)
train_data = data[:split_point]       # Split the data into training and test sets
test_data = data[split_point:]

# Separate the features (all columns except the last one) and the target variable (the last column) for both training and test sets
X_train = [row[:-1] for row in train_data]
y_train = [row[-1] for row in train_data]
X_test = [row[:-1] for row in test_data]
y_test = [row[-1] for row in test_data]

coefficients = logistic_regression(X_train, y_train)    # Train a logistic regression model using the training data


symptoms = []   # Accept user input for symptoms and validate the input
for symptom in header[:-1]:
    while True:
        # Ask the user if they have each symptom listed in the header row (all columns except the last one)
        response = input(f'Do you have {symptom}? (yes/no) ').lower()
        # If the user responds with 'yes' or 'y', append 1 to the symptoms list and break out of the while loop
        if response in {'yes', 'y'}:
            symptoms.append(1)
            break
        # If the user responds with 'no' or 'n', append 0 to the symptoms list and break out of the while loop
        elif response in {'no', 'n'}:
            symptoms.append(0)
            break
        # If the user responds with anything else, print an error message and ask again
        else:
            print('Invalid input. Please enter yes or no.')


prediction = predict([symptoms], coefficients)[0]   # Make a prediction based on the user's input symptoms using the trained logistic regression model
print(f'Prediction: {prediction}')


if prediction == 1:     # Print a message to the user based on the prediction
    print('According to the logistic regression model, you are more likely to have COVID-19.')
else:
    print('According to the logistic regression model, you are less likely to have COVID-19.')

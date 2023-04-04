import csv
import random

def separate_by_class(X_train, y_train):
    separated = {}
    for x, y in zip(X_train, y_train):
        if y not in separated:
            separated[y] = []
        separated[y].append(x)
    return separated

def summarize_dataset(dataset):
    summaries = []
    for column in zip(*dataset):
        summaries.append((min(column), max(column)))
    return summaries

def calculate_probability(x, min_value, max_value):
    smoothing_factor = 1e-9
    if x < min_value or x > max_value:
        return 0.0
    return 1.0 / (max_value - min_value + smoothing_factor)

def calculate_class_probabilities(summaries, row):
    probabilities = {}
    for class_value, class_summaries in summaries.items():
        probabilities[class_value] = 1
        for i in range(len(class_summaries)):
            min_value, max_value = class_summaries[i]
            probabilities[class_value] *= calculate_probability(row[i], min_value, max_value)
    return probabilities

def predict(summaries, row):
    probabilities = calculate_class_probabilities(summaries, row)
    best_label, best_prob = None, -1
    for class_value, probability in probabilities.items():
        if best_label is None or probability > best_prob:
            best_prob = probability
            best_label = class_value
    return best_label

def naive_bayes(X_train, y_train):
    separated = separate_by_class(X_train, y_train)
    summaries = {}
    for class_value, rows in separated.items():
        summaries[class_value] = summarize_dataset(rows)
    return summaries

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

# Train a Naive Bayes model
summaries = naive_bayes(X_train, y_train)

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
prediction = predict(summaries, symptoms)
print(f'Prediction: {prediction}')

# Print a message to the user based on the prediction
if prediction == 1:
    print('According to the Naive Bayes model, you are more likely to have COVID-19.')
else:
    print('According to the Naive Bayes model, you are less likely to have COVID-19.')

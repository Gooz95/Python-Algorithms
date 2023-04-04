import csv
import numpy as np


# Define a function to display menu for COVID-19 symptom checker
def covid_menu():
    print("=" * 33)
    print("=========Covid Diagnosis=========")
    print("=" * 33)
    positive = 0
    while True:
        try:
            age = int(input("What is your age?: "))
            break
        except ValueError:
            print("---Invalid input. Please try again using only numbers---")
    print("-" * 90)
    symptoms = []
    symptom_list = ["any previous illnesses? (e.g. asthma, diabetes)", "fever", "cough", "shortness of breath", "fatigue", "muscle or body aches", "headache", "loss of smell or taste", "sore throat", "congestion or runny nose", "nausea or vomiting", "diarrhea"]
    for symptom in symptom_list:
        while True:
            response = input(f"Do you have {symptom}? (yes/no): ").lower()
            if response in {'yes', 'y'}:
                symptoms.append(1)
                break
            elif response in {'no', 'n'}:
                symptoms.append(0)
                break
            else:
                print('Invalid input. Please enter yes or no.')
        print("-" * 90)
    # Create a list to store new patient data from covid_menu function
    new_patient = [positive, age] + symptoms
    # Return new patient data from covid_menu function
    return new_patient

new_patient = covid_menu()  # Call covid_menu function and store returned data in new_patient variable

def read_data(filename):    # Define a function to read data from a CSV file
    with open(filename, 'r') as file:   # Open the file for reading
        reader = csv.reader(file)   # Create a CSV reader object
        headers = next(reader)   # Read and store the header row
        data = []        # Create an empty list to store the data
        for row in reader:      # Loop over each row in the file
            data.append([float(value) for value in row])    # Convert row data to float and append to data list
    return headers, np.array(data)      # Return headers and numpy array of data 


# Define a function to encode categorical data in dataset 
def encode_categorical_data(data):
    # Define a list of columns that contain categorical data 
    categorical_columns = [4] + list(range(6,data.shape[1]))
    # Loop over each column in categorical_columns 
    for column in categorical_columns:
        # Find unique values in this column 
        unique_values = np.unique(data[:, column])
        # Create an empty dictionary to store mapping from unique values to integers 
        mapping = {}
        # Loop over each unique value and assign it an integer value 
        for i,value in enumerate(unique_values):
            mapping[value] = i
        # Loop over each row in data 
        for i in range(data.shape[0]):
            # Use mapping to encode categorical data for this column 
            data[i][column] = mapping[data[i][column]]
    # Return encoded data as float numpy array 
    return data.astype(float)

# Define a function to normalize numerical data in dataset 
def normalize_numerical_data(data):
    # Define a list of columns that contain numerical data 
    numerical_columns = [1]
    # Loop over each column in numerical_columns 
    for column in numerical_columns:
        # Find maximum and minimum values for this column 
        max_value = np.max(data[:, column])
        min_value = np.min(data[:, column])
        # Normalize data for this column if max_value is not equal to min_value
        if max_value != min_value:
            data[:, column] = (data[:, column] - min_value) / (max_value - min_value)
    # Return normalized data 
    return data

# Define a function to split dataset into features (x) and labels (y)
def split_data(data):
    x = data[:, 1:]
    y = data[:, 0]
    return x,y

np.random.seed(0)
# Define a function to split dataset into training and test sets
def train_test_split(x,y,test_size=0.2):
    # Create an array of indices for the rows in x
    indices = np.arange(x.shape[0])
    
    # Shuffle the indices randomly
    np.random.shuffle(indices)
    
    # Calculate number of test samples based on test_size parameter
    test_count = int(test_size * x.shape[0])
    
    # Split indices into test_indices and train_indices
    test_indices = indices[:test_count]
    train_indices = indices[test_count:]
    
    # Use train_indices and test_indices to split x and y into training and test sets 
    x_train,y_train = x[train_indices],y[train_indices]
    x_test,y_test = x[test_indices],y[test_indices]
    
    # Return training and test sets 
    return x_train,y_train,x_test,y_test

def linear_regression(x_train,y_train):
    # Define a function to perform linear regression on the training data
    x_transpose = np.transpose(x_train)    # Calculate the transpose of the x_train matrix
    weights = np.linalg.inv(x_transpose.dot(x_train)).dot(x_transpose).dot(y_train)  # Calculate the weights for the linear model using the normal equation.
    print(f'This is weights from the linear regression function before the symptom weights. {weights}')
    print(f'This is the sum of weights before the symptons weights.{sum(weights)}')

    # Define weights for each symptom based on their importance
    symptom_weights = {
        'positive': 0,
        'age': 0,
        'previously_illness': 2,
        'fever': 2,
        'cough': 2,
        'shortness_of_breath': 3, 
        'fatigue': 2,
        'muscle_or_body_aches': 1,
        'headache': 1,
        'new_loss_of_taste_or_smell': 3,
        'sore_throat': 1,
        'congestion_or_runny_nose': 1,
        'nausea_or_vomiting': 1,
        'diarrhea': 1
    }
    
    # Create a list of weights in the same order as the columns in the data
    headers = ['positive','age','previously_illness','fever','cough','shortness_of_breath','fatigue','muscle_or_body_aches','headache','new_loss_of_taste_or_smell','sore_throat','congestion_or_runny_nose','nausea_or_vomiting','diarrhea']
    symptom_weights_list = [symptom_weights[header] for header in headers]
    
    n_features = x_train.shape[1]    # Make sure that weights has shape (n_features,)
    weights[:n_features] = symptom_weights_list[:n_features]
    print(f'This is weights at the end of the function. {weights}')
    return weights    # Return the calculated weights


def predict(weights,x):  # Define a function to make predictions using the linear model
    return x.dot(weights)[0]  # Calculate and return the dot product of x and weights


filename='covid-19-dataset.csv'  # Set the filename for the dataset
headers,data=read_data(filename)  # Read in data from file using read_data function

data=encode_categorical_data(data)  # Encode categorical data in dataset using encode_categorical_data function

data=normalize_numerical_data(data)  # Normalize numerical data in dataset using normalize_numerical_data function

x,y=split_data(data)  # Split data into input and output variables using split_data function

x_train,y_train,x_test,y_test=train_test_split(x,y,test_size=0.2)  # Split data into training and test sets using train_test_split function

x_train = encode_categorical_data(x_train)  # Encode categorical data in training set
x_train = normalize_numerical_data(x_train)  # Normalize numerical data in training set

x_test = encode_categorical_data(x_test)  # Encode categorical data in test set
x_test = normalize_numerical_data(x_test)  # Normalize numerical data in test set

weights = linear_regression(x_train,y_train)    # Perform linear regression on training set to find weights for linear model

n_features = x_train.shape[1]
new_patient_array = np.array([new_patient[:n_features]])  # Create a NumPy array from new_patient variable

categorical_columns = [3] + list(range(5,x_train.shape[1]))   # Define a list of columns in the dataset that contain categorical data

for column in categorical_columns:  # Loop over each column in the list of categorical columns
    unique_values = np.unique(x_train[:, column])   # Find the unique values in this column of the training data
    mapping = {}        # Create an empty dictionary to store a mapping from unique values to integers
    for i,value in enumerate(unique_values):    # Loop over each unique value and assign it an integer value
        mapping[value] = i
    new_patient_array[0][column] = mapping[new_patient_array[0][column]]    # Use the mapping to encode the new patient's data for this column

numerical_columns = [0]  # Define a list of columns in the dataset that contain numerical data
for column in numerical_columns:  # Loop over each column in the list of numerical columns
    max_value = np.max(x_train[:,column])   # Find the maximum and minimum values for this column in the training data
    min_value = np.min(x_train[:,column])    
    # Normalize new patient's data for this column if max_value is not equal to min_value 
    if max_value != min_value:
        new_patient_array[column] = (new_patient_array[column] - min_value) / (max_value - min_value)

new_patient_prediction = predict(weights, new_patient_array)

print(f"The predicted probability of having COVID-19 is {new_patient_prediction*100:.6f}%")
print(f'{new_patient_prediction:.6f}% chance of having COVID-19')

# Print result based on prediction value 
if new_patient_prediction>5:
    print("=" * 30)
    print(f'print do if >{new_patient_prediction * 100:.6f}% chance of having COVID-19')
    print(f'print do if >{new_patient_prediction:.6f}% chance of having COVID-19')
    print('The patient is more likely to have COVID-19.')
    print("=" * 30)
else:
    print("=" * 30)
    print(f'print do else >{new_patient_prediction * 100:.6f}% chance of having COVID-19')
    print(f'print do else >{new_patient_prediction:.6f}% chance of having COVID-19')
    print('The patient is less likely to have COVID-19.')
    print("=" * 30)

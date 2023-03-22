import csv
import numpy as np


# Define a function to validate user input for yes/no questions
def ValidateStrinput(prompt):
    # Loop until valid input is received
    while True:
        try:
            # Prompt user for input and convert to string
            value = str(input(prompt))
            # Check if input is 'yes' or 'no'
            if value.lower() in ["y", "yes"]:
                return "yes"
            elif value.lower() in ["n", "no"]:
                return "no"
            else:
                # If input is not 'yes' or 'no', print error message and continue loop
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
        except ValueError:
            # If input cannot be converted to string, print error message and continue loop
            print("Invalid input. Please enter 'yes' or 'no'")
            continue

# define a function to validate the int input
def ValidateIntinput(prompt, input_type):
    # Loop until valid input is received
    while True:
        try:
            # Prompt user for input
            user_input = input_type(input(prompt))
            return user_input  # return user input
        except ValueError:  #catch the value error and print message
            print("---Invalid input. Please try again---")
            continue

# Define a function to display menu for COVID-19 symptom checker
def covid_menu():
    print("=" * 33)
    print("=========Covid Diagnosis=========")
    print("=" * 33)
    print("=" * 60)
    symptom0 = ValidateIntinput("What is your age?: ", int)
    print("-" * 60)
    symptom1 = float(ValidateStrinput("Do you have any previous illnesses? (e.g. asthma, diabetes) (yes/no): ") == "yes")
    print("-" * 60)
    symptom2 = float(ValidateStrinput("Do you have a fever? (yes/no): ") == "yes")
    print("-" * 60)
    symptom3 = float(ValidateStrinput("Do you have a cough? (yes/no): ") == "yes")
    print("-" * 60)
    symptom4 = float(ValidateStrinput("Are you experiencing shortness of breath? (yes/no): ") == "yes")
    print("-" * 60)
    symptom5 = float(ValidateStrinput("Are you feeling fatigued? (yes/no): ") == "yes")
    print("-" * 60)
    symptom6 = float(ValidateStrinput("Do you have muscle or body aches? (yes/no): ") == "yes")
    print("-" * 60)
    symptom7 = float(ValidateStrinput("Do you have a headache? (yes/no): ") == "yes")
    print("-" * 60)
    symptom8 = float(ValidateStrinput("Have you lost your sense of smell or taste? (yes/no): ") == "yes")
    print("-" * 60)
    symptom9 = float(ValidateStrinput("Do you have a sore throat? (yes/no): ") == "yes")
    print("-" * 60)
    symptom10 = float(ValidateStrinput("Do you have congestion or a runny nose? (yes/no): ") == "yes")
    print("-" * 60)
    symptom11 = float(ValidateStrinput("Do you feel nauseous or have vomiting? (yes/no): ") == "yes")
    print("-" * 60)
    symptom12 = float(ValidateStrinput("Do you have diarrhea? (yes/no): ") == "yes")
    
    
    # Create a list to store new patient data from covid_menu function
    new_patient = [symptom0, symptom1, symptom2, symptom3, symptom4,
                symptom5, symptom6, symptom7, symptom8,
                symptom9,symptom10,symptom11,symptom12]
    # Return new patient data from covid_menu function
    return new_patient

# Call covid_menu function and store returned data in new_patient variable
new_patient = covid_menu()

# Define a function to read data from a CSV file
def read_data(filename):
    # Open the file for reading
    with open(filename, 'r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)
        # Read and store the header row
        headers = next(reader)
        # Create an empty list to store the data
        data = []
        # Loop over each row in the file
        for row in reader:
            # Create an empty list to store the processed row data
            new_row = []
            # Loop over each value in the row
            for value in row:
                # Convert 'Yes' values to 1 and 'No' values to 0. Leave other values unchanged.
                if value == 'Yes':
                    new_row.append(1)
                elif value == 'No':
                    new_row.append(0)
                else:
                    new_row.append(value)
            # Append processed row data to data list
            data.append(new_row)
    # Return headers (excluding last column) and numpy array of data 
    return headers[:-1], np.array(data)

# Define a function to encode categorical data in dataset 
def encode_categorical_data(data):
    # Define a list of columns that contain categorical data 
    categorical_columns = [3] + list(range(5,data.shape[1]))
    
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
    numerical_columns = [0]
    
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
    x = data[:, :-1]
    y = data[:, -1]
    return x,y

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


def linear_regression(x_train,y_train):    # Define a function to perform linear regression on the training data
    x_transpose = np.transpose(x_train)    # Calculate the transpose of the x_train matrix
    weights = np.linalg.inv(x_transpose.dot(x_train)).dot(x_transpose).dot(y_train)  # Calculate the weights for the linear model using the normal equation
    return weights    # Return the calculated weights


def predict(weights,x):  # Define a function to make predictions using the linear model
    return x.dot(weights)  # Calculate and return the dot product of x and weights

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

weights=linear_regression(x_train,y_train)  # Perform linear regression on training set to find weights for linear model

new_patient_array = np.array(new_patient[:-1])  # Create a NumPy array from new_patient variable
# Define a list of columns in the dataset that contain categorical data
categorical_columns = [3] + list(range(5,x_train.shape[1]))

for column in categorical_columns:  # Loop over each column in the list of categorical columns
    unique_values = np.unique(x_train[:, column])   # Find the unique values in this column of the training data
    mapping = {}        # Create an empty dictionary to store a mapping from unique values to integers
    for i,value in enumerate(unique_values):    # Loop over each unique value and assign it an integer value
        mapping[value] = i
    new_patient_array[column] = mapping[new_patient_array[column]]    # Use the mapping to encode the new patient's data for this column


numerical_columns = [0]  # Define a list of columns in the dataset that contain numerical data
for column in numerical_columns:  # Loop over each column in the list of numerical columns
    max_value = np.max(x_train[:,column])   # Find the maximum and minimum values for this column in the training data
    min_value = np.min(x_train[:,column])    
    # Normalize new patient's data for this column if max_value is not equal to min_value 
    if max_value != min_value:
        new_patient_array[column] = (new_patient_array[column] - min_value) / (max_value - min_value)

# Use predict function to make prediction for new patient using trained weights and encoded/normalized new patient data 
new_patient_prediction=predict(weights,new_patient_array)

# Print result based on prediction value 
if new_patient_prediction>0.5:
    print('The patient is most likely to have COVID-19.')
else:
    print('The patient is most likely not to have COVID-19.')

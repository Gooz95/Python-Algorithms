import sys

def covid_menu():
    print("=" * 33)
    print("=========Covid Diagnosis=========")
    print("=" * 33)

    # define a function to validate the int input
    def ValidateIntinput(prompt, input_type):
        while True:
            try:
                user_input = input_type(input(prompt))
                return user_input
            except ValueError:
                print("---Invalid input. Please try again---")
                continue

    # define a function to validate the str input
    def ValidateStrinput(prompt):
        while True:
            user_input = input(prompt)
            if user_input.lower() == "yes":
                return True
            elif user_input.lower() == "no":
                return False
            else:
                print("---Invalid input Please enter 'yes' or 'no'---")
                continue

    print("-" * 60)
    symptom0 = ValidateIntinput("Enter Age: ", int)
    print("-" * 60)
    symptom1 = ValidateIntinput("Enter Blood Pressure: ", int)
    print("-" * 60)
    symptom2 = ValidateIntinput("Enter Oxygen Levels: ", int)
    print("-" * 60)
    symptom3 = ValidateStrinput("Do you have any previous illnesses? (yes/no): ")
    print("-" * 60)
    symptom4 = ValidateStrinput("Do you have a fever? (yes/no): ")
    print("-" * 60)
    symptom5 = ValidateStrinput("Do you have a cough? (yes/no): ")
    print("-" * 60)
    symptom6 = ValidateStrinput("Do you have shortness of breath? (yes/no): ")
    print("-" * 60)
    symptom7 = ValidateStrinput("Do you feel fatigued? (yes/no): ")
    print("-" * 60)
    symptom8 = ValidateStrinput("Do you have muscle or body aches? (yes/no): ")
    print("-" * 60)
    symptom9 = ValidateStrinput("Do you have a headache? (yes/no): ")
    print("-" * 60)
    symptom10 = ValidateStrinput("Do you have a new loss of taste or smell? (yes/no): ")
    print("-" * 60)
    symptom11 = ValidateStrinput("Do you have a sore throat? (yes/no): ")
    print("-" * 60)
    symptom12 = ValidateStrinput("Do you have congestion or a runny nose? (yes/no): ")
    print("-" * 60)
    symptom13 = ValidateStrinput("Do you feel nauseous or have vomiting? (yes/no): ")
    print("-" * 60)
    symptom14 = ValidateStrinput("Do you have diarrhea? (yes/no): ")
    print("=" * 60)

    # patient_symtoms = symptom0, symptom1, symptom2, symptom3, symptom4, symptom5, symptom6, symptom7, symptom8, symptom9, symptom10, symptom11, symptom12, symptom13, symptom14
    patient_symtoms = (f"Age = {symptom0}"), f"Blood Pressure = {symptom1}", (f"Oxygen Level = {symptom2}"), (f"Previous Illnesses = {symptom3}"), (f"Fever = {symptom4}"), (f"Cough = {symptom5}"), (f"Shortness of Breath = {symptom6}"), (f"Fatigued = {symptom7}"), (f"Muscle or Body aches = {symptom8}"), (f"Headache = {symptom9}"), (f"Loss of smell or taste = {symptom10}"), (f"Sore Throat = {symptom11}"), (f"Congestion or Runny nose = {symptom12}"), (f"Nauseous or Vomiting = {symptom13}"), (f"Diarrhea = {symptom14}")

    for i in patient_symtoms:
        print(i)

    while True:
        print("=" * 35)
        user_input = input("Would you like to re-enter? Y/N- ")
        if user_input.lower() == "y":
            return covid_menu()
        elif user_input.lower() == "n":
            print("=" * 30)
            print("=" * 12, "Bye", "=" * 12)
            print("=" * 30)
            return sys.exit()
        else:
            print("---Invalid input Please enter 'y' or 'n'---")
            continue
 
covid_menu()

"""
Name: Nicola
Surname: Phiri
Project Name: Task 2
Date:10 May
Term: 2
"""
from curses.ascii import isalpha

# Goal: Simple project to retrieve and display components information test data
"""Declare word for validation"""
valid = True
#Declare file
try:
         with open("components_data_ERR.txt", "x") as file:
             file.write("C101,3.3\n")
             file.write("A202,2.9\n")
             file.write("B303,error\n")
             file.write("C404,3.1\n")
             file.write("C505,\n")
             file.write("C10,3.3\n")

# Defensive programming, making sure the program doesn't shut down because of an error.
except FileExistsError:
    file = open("components_data_ERR.txt", "r")
    print("File already exists")
    file.close()

#Implement Validation and parameter
def component1(ID):
    print(f"ID: {ID}")

def component2(Voltage):
    print(f"Voltage: {Voltage}")

#Create Validation
def validate_file(line):
    components = line.strip().split(',')
    if component1() != isalpha():
        print("Not an alphaneumeric value!")

    else:
        len(components)!= 4
        return False, print("Does not contain 4 characters")

#Make sure that what has been entered is a numeric
def is_numeric():
    # Make sure that what has been entered is a numeric
    def is_numeric(voltage):
        try:
            float(voltage)
            return True
        except ValueError:
            return False
            print("Is not numeric!")

"""FIX UP THE CODE. CORRECT VALIDATION STEPS.
I THINK YOUR VALIDATIONS NEED TO BE CALLED INTO A FUNCTION.
RESEARCH IT AND SEE HOW YOU COULD INDIVIDUALLY MEET THE REQUIREMENTS FOR EACH
INDIVIDUAL VALIDATION. I DON'T THINK VALIDATION OUTSIDE A FUNCTION IS POSSIBLE."""
"""
Name: Nicola
Surname: Phiri
Project Name: Task 2
Date:15 May
Term: 2
"""

#Importing appropriate libraries for use
# Goal: Simple project to retrieve and display components information test data

#Create parameter
def components_data_ERR():
    return """C101,3.3
              A202,2.9
              B303,error
              C404,3.1
              C505
              C10,3.3"""
#Declare file & Call parameter into the text file
try:
         with open("components_data_ERR.txt", "x") as file:
             file.write(components_data_ERR())

# Defensive programming, making sure the program doesn't shut down because of an error.
except FileExistsError:
   file = open("components_data_ERR.txt", "r")
print("File already exists")
pass #That's if the file already exists

#Implement Validation
#1)Must contain numbers and must be 4 characters long
def validate_line(line):
    try:
        comp_id, voltage = line.strip().split(",")
        float(voltage) #2)check if the voltage is entered and if it's a numeric
        return len(comp_id) == 4
    except ValueError:
        return False

def line_check(input_text, validation_file="validation_file.txt"):
    results=[]
    with open(input_text, "r") as f:
        lines =f.readlines()

    with open(validation_file,"w")as f:
        for line in lines:
            is_valid = validate_line(line)
            results.append((line.strip(), is_valid))
            if not is_valid:
                f.write(f"{line.strip()}-> False\n")
    return results

results = line_check("components_data_ERR.txt")

for line, is_valid in results:
    print(f"{line}-> {is_valid}")

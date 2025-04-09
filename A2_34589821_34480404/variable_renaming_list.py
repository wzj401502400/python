"""
This program lets the user input the Python program line by line 
to analyze, and allow the user to print the program or list the 
variables.
"""

# import keyword
import keyword

# create a set to store non-repetitive variable 
variable = set()

# create a list to store program line by line
program = []

# function to print the choice menu
def print_menu():
    print("==================================")
    print("Enter your choice:")
    print("1. Print program.")
    print("2. List.")
    print("0. Quit.")
    print("==================================")

# function to check each character if valid
def check_alphabet(char):
    if (char < "a" or char > "z") and (char < "A" or char > "Z") and char != "_":
        return False
    return True

# function to check words in each line if they are valid
def check_line(line):

    # split the line into list
    line = line.split()
    
    # check each item in list
    for item in line:
        if item in keyword.kwlist:
            continue

        # set a flag about if valid
        flag = True
        
        # skip if not a valid character
        for char in item:
            if not check_alphabet(char):
                flag = False
                break
        
        # add to variable if it is valid
        if flag:
            variable.add(item)

# function to get and check input lines
def get_input():
    print("Enter the Python program to analyze, line by line. Enter 'end' to finish.")
    while True:
        line = input()

        # end the input if get the end
        if line == "end":
            break
        
        # add the line to program list and check words in line
        program.append(line)
        check_line(line)

# function to print program line by line when choosing 1
def choice_1():
    print("Program:")
    for line in program:
        print(line)

# function to sort and list the variables when choosing 2
def choice_2():
    print("Variables:")

    # change variable set to list and sort it
    list_variable = sorted(list(variable))
    for var in list_variable:
        print(var)

# function to quit the program when choosing 0
def choice_0():
    quit()

# function to print the choice menu and get the choice to handle different choice
def get_choice():
    while True:
        print_menu() 
        choice = input() 

        # handle different choice
        if choice == "0":
            choice_0()
        elif choice == "1":
            choice_1()
        elif choice == "2":
            choice_2()
        else:
            continue

# function to start the program
def start_program():
    get_input()
    get_choice()

# start program
start_program()



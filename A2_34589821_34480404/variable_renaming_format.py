"""
This program lets the user input the Python program line by line 
to analyze, and allow the user to print the program or list the 
variables or change the format of selecting existing variable 
to snake case.
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
    print("3. Format.")
    print("0. Quit.")
    print("==================================")

# function to update the new variable to the program
def add_to_program(old_var, new_var):

    # iterate each line in the program
    for i in range(len(program)):

        # search from the original position in each line
        start_point = 0

        # when the variable is existing in the line
        while program[i].find(old_var, start_point) != -1:

            # get the starting position of the old variable
            pos_start = program[i].find(old_var, start_point)

            # calculate the ending position of the old variable
            pos_end = pos_start + len(old_var)
            
            # check boundaries, the variable is the first word in this line
            if pos_start == 0:
                if check_alphabet(program[i][pos_end]):
                    
                    # change the start point and continue to search
                    start_point = pos_end
                    continue

            # check boundaries, the variable is the last word in this line
            elif pos_end == len(program[i]):
                if check_alphabet(program[i][pos_start - 1]):
                    
                    # change the start point and continue to search
                    start_point = pos_end
                    continue

            # check the variable if part of another word
            elif check_alphabet(program[i][pos_start - 1]) or check_alphabet(program[i][pos_end]):
                
                # change the start point and continue to search
                start_point = pos_end
                continue
            
            # upate the new variable in the position of the old variable to the program
            program[i] = program[i][:pos_start] + new_var + program[i][pos_end:]

# function to change the format of the variable to snake case
def change_format(var):

    # create two strings to store different stages of variable
    stage_var = ""
    new_var = ""

    # ensure the first character is lowercase
    stage_var += var[0].lower()
    stage_var += var[1:]
    
    # iterate each character in the stage variable
    for char in stage_var:

        # check if the character is an uppercase letter
        if char >= "A" and char <= "Z":

            # add an underscore before the lowercase letter
            new_var += "_"
            new_var += char.lower()
        
        # if character is not uppercase, add to the final variable 
        else:
            new_var += char
    
    # if there is no change between original and new variable, exit the function early
    if new_var == var:
        return
    
    # it exists to change, update the new variable in the variable set and program list
    variable.remove(var)
    variable.add(new_var)
    add_to_program(var, new_var)
    
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

# function to change the format of selecting the existing variable to snake case when choosing 3  
def choice_3():
    while True:
        print("Pick a variable:")

        # get the variable
        var = input()

        # check the variable if existing
        if var not in variable:
            print("This is not a variable name.")
            continue
        
        # change the format if the variable existing 
        change_format(var)
        break

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
        elif choice == "3":
            choice_3()
        else:
            continue

# function to start the program
def start_program():
    get_input()
    get_choice()

# start the program
start_program()
  

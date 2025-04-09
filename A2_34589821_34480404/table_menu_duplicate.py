"""
This program allows user to list tables or display the table or duplicate the table 
from csv files.
"""

# import tabulate and deepcopy
from tabulate import tabulate
from copy import deepcopy

# define a table class to store the content, header, and data of different tables
class Table:
    def __init__(self, content, header, data):
        self.content = content
        self.header = header
        self.data = data

    # method to list the length of column and row of the table
    def list_table(self):
        column_length = len(self.header)
        row_length = len(self.content)
        return column_length, row_length

    # method to list the specific table
    def display_table(self):
        print(tabulate(self.data, headers=self.header))

# function to print the choice menu
def print_menu():
    print("==================================")
    print("Enter your choice:")
    print("1. List tables.")
    print("2. Display table.")
    print("3. Duplicate table.")
    print("0. Quit.")
    print("==================================")

# create a list to store different csv files representing different tables
tables = ["grades.csv", "class_students.csv", "rabbytes_club_students.csv", "rabbytes_data.csv"]

# function to process all the table files, reading and splitting lines
def process_table():

    # create a list to store the table after processing
    table = []

    # iterate each csv file in the tables list
    for csv in tables:
        with open(csv, 'r') as f:

            # reading all lines in csv file
            lines = f.readlines()

            # strip spaces from strings and split them into lists by commas
            for line in range(len(lines)):
                lines[line] = lines[line].strip().split(",")

            # append lines into the tab list after processing
            table.append(lines)
    return table

# create a variable to represent the processed table 
split_tables = process_table()

# function to list tables when choosing 1
def choice_1():
    
    # set the original index and list to store all data, and header 
    index = 0
    data = []
    header = ["Index", "Columns", "Rows"]

    # iterate each table in split tables
    for table in split_tables:
        
        # list to store data in split table
        split_data = []

        # create a Table object using the content
        tab = Table(table, table[0], table[1:])
        column_length, row_length = tab.list_table()

        # append data into the split data list
        split_data.append(index)
        split_data.append(column_length)
        split_data.append(row_length)

        # store all data into whole data list
        data.append(split_data)
        index += 1

    # list tables
    print(tabulate(data, headers=header))

# function to display the table when choosing 2
def choice_2():
    
    # repeat execution if the index is not valid
    while True:
        print("Choose a table index (to display):")
        index = int(input())
        if 0 <= index <= len(split_tables) - 1:
            break
        else:
            print("Incorrect table index. Try again.")

    # define specific table
    content = split_tables[index]

    # create a Table object using the content
    tab = Table(content, content[0], content[1:])

    # use the class method to display the table
    tab.display_table()

# function to duplicate the table when choosing 3
def choice_3():

    # repeat execution if the index is not valid
    while True:
        print("Choose a table index (to duplicate):")
        index = int(input())
        if 0 <= index <= len(split_tables) - 1:
            break
        else:
            print("Incorrect table index. Try again.")

    # duplicate the target table and append it to the split tables list       
    copy_table = deepcopy(split_tables[index])
    split_tables.append(copy_table)

# function to quit the program when choosing 0
def choice_0():
    quit()

# function to print the choice menu and get the choice to handle different choice
def start_program():
    while True:
        print_menu()
        choice = input()

        # handle different choice
        if choice == "1":
            choice_1()
        elif choice == "2":
            choice_2()
        elif choice == "3":
            choice_3()
        elif choice == "0":
            choice_0()
        else:
            continue

# start program
start_program()


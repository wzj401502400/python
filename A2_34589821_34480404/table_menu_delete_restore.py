"""
This program allows user to list tables or display the table or duplicate the table 
or create the table or delete the table or delete the column or restore the table 
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
    print("4. Create table.")
    print("5. Delete table.")
    print("6. Delete column.")
    print("7. Restore table.")
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
        
        # skip this index if it belongs to the delete table
        if index in delete_tables:
            index += 1
            continue
        
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

# function to display table when choosing 2
def choice_2():
    
    # repeat execution if the index is not valid
    while True:
        print("Choose a table index (to display):")
        index = int(input())
        if 0 <= index <= len(split_tables) - 1 and index not in delete_tables:
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
        if 0 <= index <= len(split_tables) - 1 and index not in delete_tables:
            break
        else:
            print("Incorrect table index. Try again.")

    # duplicate the target table and append it to the split tables list       
    copy_table = deepcopy(split_tables[index])
    split_tables.append(copy_table)

# function to create the table when choosing 4
def choice_4():

    # repeat execution if the index is not valid
    while True:
        print("Choose a table index (to create from):")
        index = int(input())
        if 0 <= index <= len(split_tables) - 1 and index not in delete_tables:
            break
        else:
            print("Incorrect table index. Try again.")

    # input columns and split it into the list by comma
    print("Enter the comma-separated indices of the columns to keep:")
    columns = input().split(',')

    # get the target table
    target_table = deepcopy(split_tables[index])
    new_table = []

    # iterate each line in target table
    for line in target_table:
        new_line = []

        # iterate each column and append the value at the specific column to the new line
        for col in columns:
            new_line.append(line[int(col)])
        new_table.append(new_line)
    
    # append the new table to the split tables list
    split_tables.append(new_table)

# create a list to store the index of deleted tables
delete_tables = []

# function to delete the table when choosing 5
def choice_5():

    # repeat execution if the index is not valid 
    while True:
        print("Choose a table index (for table deletion):")
        index = int(input())
        if 0 <= index <= len(split_tables) - 1 and index not in delete_tables:
            break
        else:
            print("Incorrect table index. Try again.")

    # append the index to the delete tables list
    delete_tables.append(index)

# function to delete the column when choosing 6
def choice_6():

    # repeat execution if the index is not valid 
    while True:
        print("Choose a table index (for column deletion):")
        index = int(input())
        if 0 <= index <= len(split_tables) - 1 and index not in delete_tables:
            break
        else:
            print("Incorrect table index. Try again.")

    # input columns and split it into the list by comma
    print("Enter the index of the column to delete:")
    columns = input().split(",")

    # iterate each row in the selected table
    for i, line in enumerate(split_tables[index]):

        # iterate each column in the provided column and remove the target column in the line
        for col in columns:
            line.remove(line[int(col)])

# function to restore the table when choosing 7
def choice_7():

    # repeat execution if the index is not valid 
    while True:
        print("Choose a table index (for restoration):")
        index = int(input())
        if 0 <= index <= len(split_tables) - 1 and index in delete_tables:
            break
        else:
            print("Incorrect table index. Try again.")

    # remove the index from the delete tables list
    delete_tables.remove(index)

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
        elif choice == "4":
            choice_4()
        elif choice == "5":
            choice_5()
        elif choice == "6":
            choice_6()
        elif choice == "7":
            choice_7()
        elif choice == "0":
            choice_0()
        else:
            continue

# start program
start_program()

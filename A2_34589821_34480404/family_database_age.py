"""
This program stores and lists the names and ages of different rabbits.
"""

# create the class to get and store rabbit names and age
class Rabbytes:
    def __init__(self, name, age = "Unknown"):
        self.name = name
        self.age = age

# create a customizable class to show print sentences in different situations  
class Print:
    pass

    # method to print choice greeting
    def choice(self): 
        print("==================================")
        print("Enter your choice:")
        print("1. Create a Rabbit.")
        print("2. Input Age of a Rabbit.")
        print("3. List Rabbytes.")
        print("0. Quit.")
        print("==================================")

    # method to print new rabbit name
    def new_name(self):
        print("Input the new rabbit's name:")

    # method to print the existing rabbit name
    def old_name(self):
        print("Input the rabbit's name:")

    # method to print the specific rabbit age
    def age(self, name):
        print(f"Input {name}'s age:")
    
    # method to print nonexistent reminder
    def non_exist(self):
        print("That name is not in the database.")

    # method to print existing reminder
    def exist(self):
        print("That name is already in the database.")
        
# create a customizable class to get a list of rabbit names
class Name:
    pass

    # method to get a list of rabbit names
    def get_names(self, rabbytes):
        names = []
        for rabbit in rabbytes:
            names.append(rabbit.name)
        return names

# create a list to store class object
rabbytes = []

# create objects for class
pri = Print()
nam = Name()

# set a loop to repeat the choice
while True:

    # get the choice 
    pri.choice()
    choice = input()

    # quit the program when choosing 0        
    if choice == "0":
        quit()

    # create and store the nonexistent new rabbit name when choosing 1 
    elif choice == "1":
        while True:

            # reminder and get rabbit name
            pri.new_name()
            name = input()

            # remind existent and repeat execution if repeating the name
            if name in nam.get_names(rabbytes):
                pri.exist()
                continue
            
            # create a new instance and store it in list 
            new_name=Rabbytes(name)
            rabbytes.append(new_name)
            break

    # create and update the age for the existent rabbit when choosing 2
    elif choice == "2":
        while True:

            # reminder and get the rabbit name
            pri.old_name()
            name = input()
                
            # remind nonexistent and repeat execution if get the unknown name 
            if name not in nam.get_names(rabbytes):
                pri.non_exist()
                continue

            # get and update the age for specific rabbits in the list 
            pri.age(name)
            age = input()
            for rabbit in rabbytes:
                if rabbit.name == name:
                    rabbit.age = age
            break

    # list all names and ages of existent rabbits when choosing 3
    elif choice == "3":
        print("Rabbytes:")

        # use stored information in the list to show 
        for rabbit in rabbytes:
            print (f"{rabbit.name} ({rabbit.age})")

"""
This program stores and lists the names and ages of different rabbits, 
creates parental relationships and lists existing rabbits' direct
family relationships and lists of cousins of specific rabbit.
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
        print("4. Create a Parental Relationship.")
        print("5. List Direct Family of a Rabbit.")
        print("6. Find Cousins of a Rabbit.")
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

    # method to print parent name
    def parent(self):
        print("Input the parent's name:")

    # method to print kitten name
    def kitten(self):
        print("Input the kitten's name:")
    
    # method to print specific parent name
    def parents_name(self, name):
        print(f"Parents of {name}:")

    # method to print specific kitten name
    def kittens_name(self, name):
        print(f"Kittens of {name}:")

    def cousins_name(self, name):
        print(f"Cousins of {name}:")
        
# create a customizable class to get a list of rabbit names
class Name:
    pass

    # method to get a list of rabbit names
    def get_names(self, rabbytes):
        names = []
        for rabbit in rabbytes:
            names.append(rabbit.name)
        return names

# create a class to get and sort and print the parent and kitten names
class Family:

    # initialize object with name and empty lists for parents and kittens and cousins
    def __init__(self, my_name):
        self.my_name = my_name
        self.parent = []
        self.kitten = []

    # method to print all the parent names
    def get_parents(self):
        for par in self.parent:
            print(par)

    # method to print all the kitten names
    def get_kittens(self):
        for kit in self.kitten:
            print(kit)

    # method to get the cousin names
    def get_cousins(self):

        # create three lists for storing grandparents, parents, and cousins of rabbits
        grandparent = []
        parent = []
        cousin = []

        # create the loop to get the grandparents of current parents and add them into grandparent list
        for par in self.parent:
            for fam in family:
                if par == fam.my_name:
                    grandparent += fam.parent

        # use a set to remove duplicate names from the grandparent list and sort it
        grandparent = set(grandparent)
        grandparent = sorted(list(grandparent))

        # create the loop to get all kittens of current grandparents and add them into parent list
        for gra in grandparent:
            for fam in family:
                if gra == fam.my_name:
                    parent += fam.kitten

        # use a set to remove duplicate names from the parent list and sort it
        parent = set(parent)
        parent = sorted(list(parent))

        # create the loop to get all kittens of current parents and add them into cousin list
        for par in parent:

            # exclude current rabbit's parents
            if par not in self.parent:
                for fam in family:
                    if par == fam.my_name:
                        cousin += fam.kitten

        # use a set to remove duplicate names from the cousin list and sort it
        cousin = set(cousin)
        cousin = sorted(list(cousin))

        # use the loop to print all cousin names
        for con in cousin:
            print(con)

    # method to ensure add new parent names and sort the list
    def set_parents(self, name):
        if name not in self.parent:
            self.parent.append(name)
        self.parent = sorted(self.parent)

    # method to ensure add new kitten names and sort the list
    def set_kittens(self, name):
        if name not in self.kitten:
            self.kitten.append(name)
        self.kitten = sorted(self.kitten)

# create a list to store class object
rabbytes = []
family = []

# create object for class
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

            # create new instances and store it in lists 
            new_name = Rabbytes(name)
            new_family = Family(name)
            rabbytes.append(new_name)
            family.append(new_family)
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

    # create the relationship between rabbits when choosing 4
    elif choice == "4":

        # get parent and kitten name
        pri.parent()
        parent_name = input()
        pri.kitten()
        kitten_name = input()

        # add parent if the parent do not exist in the list
        if parent_name not in nam.get_names(rabbytes):
            parent = Rabbytes(parent_name)
            rabbytes.append(parent)

        # add kitten if the kitten do not exist in the list
        if kitten_name not in nam.get_names(rabbytes):
            kitten = Rabbytes(kitten_name)
            rabbytes.append(kitten)

        # set two variables to add the nonexistent condition for parent and kitten in the list   
        fam_parent = ""
        fam_kitten = ""

        # check the list to find the object for the parent
        for fam in family:
            if fam.my_name == parent_name:
                fam_parent = fam
        
        # if parent can not be found, create a new one and add it to the family list
        if fam_parent == "":
            fam_parent = Family(parent_name)
            family.append(fam_parent)

        # add the kitten to the parent object in the list and sort the list
        fam_parent.set_kittens(kitten_name)

        # check the list to find the object for the kitten
        for fam in family:
            if fam.my_name == kitten_name:
                fam_kitten = fam

        # if kitten can not be found, create a new one and add it to the family list
        if fam_kitten == "":
            fam_kitten = Family(kitten_name)
            family.append(fam_kitten)

        # add the parent to the kitten object in the list and sort the list
        fam_kitten.set_parents(parent_name)
        
    # list the direct family of existing rabbits when choosing 5
    elif choice == "5":
        while True:

            # get the name and check if exists in the list
            pri.old_name()
            name = input()

            # reinput the name if get nonexistent name
            if name not in nam.get_names(rabbytes):
                pri.non_exist()
                continue

            # find the specific object in the family list for the given name 
            for fam in family:
                if fam.my_name == name:
                    target_fam = fam

            # print parents of specific rabbit
            pri.parents_name(name)
            target_fam.get_parents()

            # print kittens of specific rabbit
            pri.kittens_name(name)
            target_fam.get_kittens()    
            break

    elif choice == "6":
        while True:

            # get the name and check if exists in the list
            pri.old_name()
            name = input()

            # reinput the name if get nonexistent name
            if name not in nam.get_names(rabbytes):
                pri.non_exist()
                continue

            # find the specific object in the family list for the given name 
            for fam in family:
                if fam.my_name == name:
                    target_fam = fam  

            # print cousins of specific rabbit
            pri.cousins_name(name)
            target_fam.get_cousins()
            break
            

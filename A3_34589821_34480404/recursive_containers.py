"""
This program reads items and containers from five csv files, containers can be items, 
allows the user to pick a container from containers and multi containers 
and magic containers and magic multi compartments to loot items and list the looted items.
"""

# import deepcopy
from copy import deepcopy

class Item:
    """
    A representation of the item.
    """
    def __init__(self, name, weight):
        """
        Creates an item with name and weight.

        Parameters:
            name (str): The name of the item.
            weight (int or str): The weight of the item.
        """
        self.name = name
        self.weight = int(weight)

    def __str__(self) -> str:
        """
        Returns a string representing of the Item.
        @return a string representing the Item.
        """
        return f"{self.name} (weight: {self.weight})"
        
    def display(self, space) -> None:
        """
        Displays the item's details.

        Parameters:
            space (str): A string used for formatting the display output.
        """
        print(space + self.__str__())
    
    def is_magic(self) -> bool:
        """
        Returns the item is not magic.
        @return the bool representing the item is not magic.
        """
        return False

class Container:
    """
    A representation of the container.
    """
    def __init__(self, name, empty_weight, weight_capacity):
        """
        Creates a container with name, empty weight, and weight capacity.

        Parameters:
            name (str): The name of the container.
            empty_weight (int or str): The weight of the empty container.
            weight_capacity (int or str): The maximum weight capacity of the container.
            weight (int or str): The total weight of the container.
            current_capacity (int): The weight of items in the container.
            compartment (list): The list of items and containers in the container.
        """
        self.name = name
        self.empty_weight = int(empty_weight)
        self.weight_capacity = int(weight_capacity)
        self.weight = self.empty_weight
        self.current_capacity = 0

        # list to store items and containers in the compartment
        self.compartment = []

    def __str__(self) -> str:
        """
        Returns a string representing of the Container.
        @return a string representing the Container.
        """
        return f"{self.name} (total weight: {self.weight}, empty weight: {self.empty_weight}, capacity: {self.current_capacity}/{self.weight_capacity})"

    def add_item_flag(self, item) -> bool:
        """
        Attempts to add an item to the container.
        
        Parameters:
            item (Item): The item to add to the container.
            
        @return the bool: True if the item can be added, False otherwise.
        """
        # check if the item can be added in the container itself
        if item.weight <= self.weight_capacity - self.current_capacity:
            self.compartment.append(deepcopy(item))
            self.weight += item.weight
            self.current_capacity += item.weight 
            return True
        else:
            # check if the item can be added in a nested magic container
            return self.check_magic_container(deepcopy(item))
            
    # method to display all items in the container by formatting
    def display(self, space) -> None:
        """
        Displays the container's details and its items.

        Parameters:
            space (str): A string used for formatting the display output.
        """
        print(space + self.__str__())
        space += "   "
        for element in self.compartment:
            element.display(space)

    def check_magic_container(self, item) -> bool:
        """
        Checks if a given item can be added to a magic compartment.

        Parameters:
            item (Item): The item to be checked for addition to the magic container.

        @return a bool telling if the item can be added to a magic compartment.
        """
        for element in self.compartment:
            if element.is_magic():
                if element.add_item_flag(deepcopy(item)):
                    return True
        return False

    def is_magic(self) -> bool:
        """
        Returns the container is not magic.
        @return the bool representing the container is not magic.
        """
        return False

class MultiContainer(Container):
    """
    A representation of the multi-container that can hold multiple containers.
    """

    def __init__(self, name, compartment):
        """
        Creates a multi-container with a name and a list of compartments.

        Parameters:
            name (str): The name of the MultiContainer.
            compartment (list): A list of Container objects that the MultiContainer holds.
        """
        super().__init__(name, 0, 0)
        self.compartment = compartment

        # iterate each container in the compartment and update the empty weight and weight
        for container in compartment:
            self.empty_weight += container.empty_weight
        self.weight = self.empty_weight

    def __str__(self) -> str:
        """
        Returns a string representation of the MultiContainer.
        @return a string representing the MultiContainer.
        """
        return f"{self.name} (total weight: {self.weight}, empty weight: {self.empty_weight}, capacity: {self.current_capacity}/{self.weight_capacity})"

    def add_item_flag(self, item) -> bool:
        """
        Attempts to add an item to one of the containers in the multi-container.

        Parameters:
            item (Item): The item to add.

        @return the bool: True if the item can be added to one of the compartments, False otherwise.
        """
        for container in self.compartment:

            # check if the item can be added in the container of the compartment
            if container.add_item_flag(deepcopy(item)):

                # update the total weight and return True if the item can be added
                self.weight += item.weight
                return True

        return False

    def display(self, space) -> None:
        """
        Displays the multi-container's details and its compartments.

        Parameters:
            space (str): A string used for formatting the display output.
        """
        print(space + self.__str__())
        space += "   "
        for container in self.compartment:
            container.display(space)

class MagicContainer(Container):
    """
    A representation of the MagicContainer that can hold multiple containers.
    """

    def __init__(self, name, compartment):
        """
        Initializes a MagicContainer instance.

        Parameters:
            name (str): The name of the MagicContainer.
            compartment (list): A list of Container objects that this MagicContainer will hold.
        """
        super().__init__(name, 0, 0)
        self.compartment = compartment
        self.current_capacity = 0

        for container in compartment:
            self.empty_weight += container.empty_weight
            self.weight_capacity += container.weight_capacity

        self.weight = self.empty_weight
    
    def __str__(self) -> str:
        """
        Returns a string representation of the MagicContainer.
        @return a string representing the MagicContainer.
        """
        return f"{self.name} (total weight: {self.weight}, empty weight: {self.empty_weight}, capacity: {self.current_capacity}/{self.weight_capacity})"

    def add_item_flag(self, item) -> bool:
        """
        Attempts to add an item to one of the containers in the compartment.

        Parameters:
            item (Item): The item to add to the MagicContainer.

        @return the bool: True if the item was successfully added to a container, False otherwise.
        """
        for container in self.compartment:
            # check if the item can be added in the container itself
            if item.weight <= self.weight_capacity - self.current_capacity:
                container.compartment.append(deepcopy(item))
                self.current_capacity += item.weight
                return True
            else:
                return self.check_magic_container(item)

    def display(self, space) -> None:
        """
        Displays the details of the MagicContainer and its compartments.

        Parameters:
            space (str): A string used for formatting the display output.
        """
        print(space, end="")
        print(self.__str__())
        space += "   "
        for container in self.compartment:
            for element in container.compartment:
                element.display(space)

    def check_magic_container(self, item) -> bool:
        """
        Checks if a given item can be added to a magic compartment.

        Parameters:
            item (Item): The item to be checked for addition to the magic container.

        @return a bool telling if the item can be added to a magic compartment.
        """
        for container in self.compartment:
            for element in container.compartment:
                if element.is_magic():
                    if element.add_item_flag(item):
                        return True

        return False
                    
    def is_magic(self) -> bool:
        """
        Returns the MagicContainer is magic.
        @return the bool representing the MagicContainer is magic.
        """
        return True

class MagicMultiContainer(MagicContainer):
    """
    A representation of the MagicMultiContainer that can hold multiple MagicContainers.
    """

    def __init__(self, name, compartment):
        """
        Initializes a MagicMultiContainer instance.

        Parameters:
            name (str): The name of the MagicContainer.
            compartment (list): A list of Container objects that this MagicContainer will hold.
        """
        super().__init__(name, compartment)

    def __str__(self) -> str:
        """
        Returns a string representation of the MagicMultiContainer.
        @return a string representing the MagicMultiContainer.
        """
        return f"{self.name} (total weight: {self.weight}, empty weight: {self.empty_weight}, capacity: {self.current_capacity}/{self.weight_capacity})"
        
    def add_item_flag(self, item) -> bool:
        """
        Attempts to add an item to one of the MagicContainers in the compartment.

        Parameters:
            item (Item): The item to add to the MagicMultiContainer.

        @return the bool: True if the item was successfully added to a MagicContainer, False otherwise.
        """
        for multi_container in self.compartment:
            for element in multi_container.compartment:
                if element.add_item_flag(deepcopy(item)):
                    # return True if the item can be added
                    return True

        return False
     
    def display(self, space) -> None:
        """
        Displays the details of the MagicMultiContainer and its compartments.

        Parameters:
            space (str): A string used for formatting the display output.
        """
        print(space + self.__str__())
        space += "   "
        for multi_container in self.compartment:
            for element in multi_container.compartment:
                element.display(space)

def read_items() -> list:
    """
    Reads and returns all items from the items.csv file.
    @return a list representing a sorted list of Item objects.
    """
    items = []
    with open("items.csv", "r") as file_items:
        lines = file_items.readlines()

        # split each line into name and weight, store the item object into the item list  
        for line in lines[1:]:    
            name, weight = line.strip().split(",")  
            items.append(Item(name.strip(), weight.strip()))
    
    items.sort(key=lambda item: item.name)
    return items

def read_containers() -> list:
    """
    Reads and returns all containers from the containers.csv file.
    @return a list representing a sorted list of Container objects.
    """
    containers = []
    with open("containers.csv", "r") as file_containers:
        lines = file_containers.readlines()

        # split each line into name and empty weight and weight capacity, store the container object into the container list  
        for line in lines[1:]:
            name, empty_weight, weight_capacity = line.strip().split(", ")
            containers.append(Container(name, empty_weight, weight_capacity))

    containers.sort(key=lambda container: container.name)
    return containers

def read_multi_containers() -> list:
    """
    Reads and returns all multi-containers from the multi_containers.csv file.
    @return a list representing a sorted list of MultiContainer objects.
    """
    multi_containers = []

    with open("multi_containers.csv", "r") as file_multi_containers:
        lines = file_multi_containers.readlines()

        for line in lines[1:]:
            compartments = []

            name = line.strip().split(",")[0]
            compartment = line.strip().split(",")[1:]

            for com in compartment:
                for container in containers:
                    if container.name == com.strip():
                        
                        # store the container data in the compartment list
                        compartments.append(deepcopy(container))

            multi_containers.append(deepcopy(MultiContainer(name, compartments)))

    multi_containers.sort(key=lambda container: container.name)
    return multi_containers

def read_magic_containers() -> list:
    """
    Reads and returns all MagicContainer objects from the magic_containers.csv file.
    @return a sorted list representing MagicContainer objects.
    """
    with open("magic_containers.csv", "r")as file_magic_containers:
        lines = file_magic_containers.readlines()
        magic_containers = []

        for line in lines[1:]:
            compartments = []
            name = line.strip().split(",")[0]
            compartment = line.strip().split(",")[1:]

            for com in compartment:
                for container in containers:
                    if container.name == com.strip():
                        compartments.append(deepcopy(container))

            magic_containers.append(deepcopy(MagicContainer(name, compartments)))

    magic_containers.sort(key=lambda container: container.name)
    return magic_containers

def read_magic_multi_containers() -> list:
    """
    Reads and returns all MagicMultiContainer objects from the magic_multi_containers.csv file.
    @return a list representing a sorted list of MagicMultiContainer objects.
    """
    with open("magic_multi_containers.csv", "r") as file_magic_containers:
        lines = file_magic_containers.readlines()
        magic_multi_containers = []
        
        for line in lines[1:]:
            compartments = []
            name = line.strip().split(",")[0]
            compartment = line.strip().split(",")[1:]

            for com in compartment:
                for container in containers:
                    if container.name == com.strip():

                        # store the container data in the compartment list
                        compartments.append(deepcopy(container))

            magic_multi_containers.append(deepcopy(MagicMultiContainer(name, compartments)))

    magic_multi_containers.sort(key=lambda container: container.name)
    return magic_multi_containers

def print_menu() -> None:
    """
    Displays the menu options for the user.
    """
    print("==================================")
    print("Enter your choice:")
    print("1. Loot item.")
    print("2. List looted items.")
    print("0. Quit.")
    print("==================================")

def loot_item(main_container) -> None:
    """
    Allows the user to loot an item into the specified container.

    Parameters:
        container_name (str): The name of the container where the item will be looted.
    """
    element = None
    container_flag = False
    while True:
        item_name = input("Enter the name of the item: ")
        item_flag = False
        
        # check if it is an item
        for item in items:
            if item_name == item.name:
                item_flag = True
                element = deepcopy(item)
                break

        # check if it is a container
        for container in containers:
            if item_name == container.name:
                item_flag = True
                element = deepcopy(container)
                break
        
        # continue to try until a valid item name
        if not item_flag:
            print(f"\"{item_name}\" not found. Try again.")
            continue
        break

    # try to add the item in the container and get the boolean result 
    container_flag = main_container.add_item_flag(deepcopy(element))
    
    if container_flag:
        print(f"Success! Item \"{item_name}\" stored in container \"{main_container.name}\".")
    else:
        print(f"Failure! Item \"{item_name}\" NOT stored in container \"{main_container.name}\".")

def list_looted_item(main_container) -> None:
    """
    Lists all looted items in the specified container.

    Parameters:
        container_name (str): The name of the container to list items from.
    """
    # display the contents of the matching container
    main_container.display("")

def start_program():
    """
    Starts the user interaction and manages the program flow.
    """
    print("Initialised 60 items including 28 containers.")
    print("")
    main_container = None
    
    # loop until it gets a valid container name
    while True:
        container_name = input("Enter the name of the container: ")
        container_flag = False

        # iterate each container in the container list
        for container in containers:
            if container_name == container.name:
                container_flag = True
                main_container = deepcopy(container)
                break

        # continue to try until it gets a valid container name
        if not container_flag:
            print(f"{container_name} not found. Try again")  
            continue
        break

    # loop to print the meun and get the user choice 
    while True:
        print_menu()
        choice = input()

        if choice == "0":
            quit()
        elif choice == "1":
            loot_item(main_container)
        elif choice == "2":
            list_looted_item(main_container)
        else:
            continue

# main operations
items = read_items()
containers = read_containers()
multi_containers = read_multi_containers()
containers += multi_containers
magic_containers = read_magic_containers()
containers += magic_containers
magic_multi_containers = read_magic_multi_containers()
containers += magic_multi_containers

# start the program
start_program()

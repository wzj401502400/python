"""
This program reads items and containers from two csv files, 
allows the user to pick a container from containers 
to loot items and list the looted items.
"""

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
            total_weight (int or str): The total weight of the container.
            current_capacity (int): The weight of items in the container.
        """
        self.name = name
        self.empty_weight = int(empty_weight)
        self.weight_capacity = int(weight_capacity)
        self.total_weight = self.empty_weight
        self.current_capacity = 0

        # list to store items in the containers
        self.items = []

    def __str__(self) -> str:
        """
        Returns a string representing of the Container.
        @return a string representing the Container.
        """
        return f"{self.name} (total weight: {self.total_weight}, empty weight: {self.empty_weight}, capacity: {self.current_capacity}/{self.weight_capacity})"
    
    def add_item_flag(self, item) -> bool:
        """
        Attempts to add an item to the container.
        
        Parameters:
            item (Item): The item to add to the container.
            
        @return the bool: True if the item can be added, False otherwise.
        """
        # if there is enough weight capacity, add the item in the container and update the data of the container
        if item.weight <= self.weight_capacity - self.current_capacity:
            self.items.append(item)
            self.total_weight += item.weight
            self.current_capacity += item.weight
            return True
        
        return False

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
            name, weight = line.strip().split(", ")  
            items.append(Item(name, weight))
    
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

def loot_item(container_name) -> None:
    """
    Allows the user to loot an item into the specified container.

    Parameters:
        container_name (str): The name of the container where the item will be looted.
    """
    while True:
        item_name = input("Enter the name of the item: ")
        item_flag = False
        
        # Iterate through items to check for validity
        for item in items:
            if item_name == item.name:
                item_flag = True
                break
        
        # continue to try until a valid item name
        if not item_flag:
            print(f"\"{item_name}\" not found. Try again.")
            continue
        break

    for container in containers:
        if container_name == container.name:
            
            # try to add the item in the container and get the boolean result 
            container_flag = container.add_item_flag(item)
    
    if container_flag:
        print(f"Success! Item \"{item_name}\" stored in container \"{container_name}\".")
    else:
        print(f"Failure! Item \"{item_name}\" NOT stored in container \"{container_name}\".")
   
def list_looted_items(container_name) -> None:
    """
    Lists all looted items in the specified container.

    Parameters:
        container_name (str): The name of the container to list items from.
    """
    for container in containers:
        if container_name == container.name:
            print(container.__str__())

            for item in container.items:
                print("   " + item.__str__())

def start_program() -> None:
    """
    Starts the user interaction and manages the program flow.
    """
    print("Initialised 47 items including 15 containers.")
    print("")
    
    # loop until it gets a valid container name
    while True:
        container_name = input("Enter the name of the container: ")
        container_flag = False

        for container in containers:
            if container_name == container.name:
                container_flag = True
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
            loot_item(container_name)
        elif choice == "2":
            list_looted_items(container_name)
        else:
            continue

# main operations
items = read_items()
containers = read_containers()

# start the program
start_program()

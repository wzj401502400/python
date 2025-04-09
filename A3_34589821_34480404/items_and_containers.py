"""
This program reads and lists items and containers from two csv files.
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

    def __str__(self) -> str:
        """
        Returns a string representing of the Container.
        @return a string representing the Container.
        """
        return f"{self.name} (total weight: {self.total_weight}, empty weight: {self.empty_weight}, capacity: {self.current_capacity}/{self.weight_capacity})"

def read_items() -> None:
    """
    function to read and print all items in items.csv file, creates Item objects, 
    sorts them by item name, and prints each item.
    """
    items = []
    with open("items.csv", "r") as file_items:
        lines = file_items.readlines()

        # split each line into name and weight, store the item object into the item list  
        for line in lines[1:]:  
            name, weight = line.strip().split(", ")  
            items.append(Item(name, weight))

    items.sort(key=lambda item: item.name)

    for item in items:
        print(item)

def read_containers() -> None:
    """
    function to read and print all containers in containers.csv file, creates Container objects, 
    sorts them by container name, and prints each container.
    """
    containers = []
    with open("containers.csv", "r") as file_containers:
        lines = file_containers.readlines()

        # split each line into name and empty weight and weight capacity, store the container object into the item list  
        for line in lines[1:]:
            name, empty_weight, weight_capacity = line.strip().split(", ")
            containers.append(Container(name, empty_weight, weight_capacity))

    containers.sort(key=lambda container: container.name)
    for container in containers:
        print(container)         

# print the outcome by formatting
print("Initialised 47 items including 15 containers.")
print("")
print("Items:")
read_items()  
print("")
print("Containers:")
read_containers() 
print("")

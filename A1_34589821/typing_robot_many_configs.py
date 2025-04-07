"""
This is a login program which commands robot 
to outcome the string by fewest operation and
output the configuration and action steps.
"""

# get the string
string=input("Enter a string to type: ")

# set four lists for four different configurations
Configuration_0=["abcdefghijklm",
                 "nopqrstuvwxyz"]

Configuration_1=["789",
                 "456",
                 "123",
                 "0.-"]

Configuration_2=["chunk",
                 "vibex",
                 "gymps",
                 "fjord",
                 "waltz"]

Configuration_3=["bemix",
                 "vozhd",
                 "grypt",
                 "clunk",
                 "waqfs"]

# set position function to get string position and type of Configuration
def position_Configuration(x,Configuration):

    # y means every possible rows, Configuration refers four different configurations
    for y in range(len(Configuration)):

        # if x exists in the configuration, y means every possible rows in this Configuration
        if x in Configuration[y]:
    
                # confirm the coordinate
                return (Configuration[y].index(x),y)

    # returns None if it does not appear in the Configuration
    return None

# set function to define robot action about Configuration
def robot_action_Configuration(step,Configuration):

    # set original coordinate and an empty robot action list
    robot_x,robot_y=(0,0)
    robot_action_Configuration=[]

    # step means loop every letter in the string 
    for step in string:

        # if can not confirm the coordinate by position function, return ""
        if position_Configuration(step,Configuration) == None:
            return ""

        # if coordinate can be confirmed, confirm target coordinate by position function
        target_position_Configuration=position_Configuration(step,Configuration)

        # set represent coordinate for target coordinate
        target_x,target_y=target_position_Configuration

        # left, right, down, up, moving rules depend on specific condition
        if robot_x > target_x:
            robot_action_Configuration.append("l"*(robot_x-target_x))

        elif robot_x < target_x:
            robot_action_Configuration.append("r"*(target_x-robot_x))

        if robot_y < target_y:
            robot_action_Configuration.append("d"*(target_y-robot_y))

        elif robot_y > target_y:
            robot_action_Configuration.append("u"*(robot_y-target_y))

        # when robot reaches the target coordinate, press "p"
        robot_x,robot_y=target_x,target_y
        robot_action_Configuration.append("p")

    # turn robot action list into string after the loop
    return "".join(robot_action_Configuration)


# reintroduce function and get robot actions depends on four different Configurations
robot_action_0=robot_action_Configuration(string,Configuration_0)
robot_action_1=robot_action_Configuration(string,Configuration_1)
robot_action_2=robot_action_Configuration(string,Configuration_2)
robot_action_3=robot_action_Configuration(string,Configuration_3)

# calculate the length respectively
length_robot_0=len(robot_action_0)
length_robot_1=len(robot_action_1)
length_robot_2=len(robot_action_2)
length_robot_3=len(robot_action_3)

# if the length can not be cauculated by each Configuration, output the outcome
if length_robot_0 == 0 and length_robot_1 == 0 and length_robot_2 == 0 and length_robot_3 == 0:
    print("The string cannot be typed out.")
else:
    # if it belongs to Configuration_1, output the outcome
    if length_robot_1 != 0:
        print("Configuration used:")
        print("-------")
        print("| 789 |\n| 456 |\n| 123 |\n| 0.- |")
        print("-------")
        print("The robot must perform the following operations:")
        print(robot_action_1)
    
    # exclude 0 length, use configuration_2 if it is the fewest steps or equal to configuration_3 both the fewest steps
    elif length_robot_2 != 0 and (length_robot_2 < length_robot_0 or length_robot_0 == 0) and (length_robot_2 <= length_robot_3 or length_robot_3 == 0):
        print("Configuration used:")
        print("---------")
        print("| chunk |\n| vibex |\n| gymps |\n| fjord |\n| waltz |")
        print("---------")
        print("The robot must perform the following operations:")
        print(robot_action_2)

    # exclude 0 length and appearing equal fewest steps in other configuration, use configuration_3 if it is fewest steps
    elif length_robot_3 != 0 and (length_robot_3 < length_robot_0 or length_robot_0 == 0) and (length_robot_3 < length_robot_2 or length_robot_2 == 0):
        print("Configuration used:")
        print("---------")
        print("| bemix |\n| vozhd |\n| grypt |\n| clunk |\n| waqfs |")
        print("---------")
        print("The robot must perform the following operations:")
        print(robot_action_3)
    
    # exclude 0 length, use configuration_0 if configuration_0 gets the fewest steps and equal to other configuration as well
    elif length_robot_0 != 0 or length_robot_0 == length_robot_2 or length_robot_0 == length_robot_3:
        print("Configuration used:")
        print("-----------------")
        print("| abcdefghijklm |\n| nopqrstuvwxyz |")
        print("-----------------")
        print("The robot must perform the following operations:")
        print(robot_action_0)

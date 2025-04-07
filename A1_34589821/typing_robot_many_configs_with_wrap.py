"""
This is a login program with adding new moving rules,
it commands robot to outcome the string by fewest 
operation and output the configuration and action steps.
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

    # set loop in every possible Configuration
    for y in range(len(Configuration)):

        # if x exists in the configuration
        if x in Configuration[y]:

                # confirm the coordinate
                return (Configuration[y].index(x),y)

    # returns None if it does not appear in the Configuration
    return None

# get x: row length, y: column length for each Configuration
x_length_0=len(Configuration_0[0])
y_length_0=len(Configuration_0)

x_length_1=len(Configuration_1[0])
y_length_1=len(Configuration_1)

x_length_2=len(Configuration_2[0])
y_length_2=len(Configuration_2)

x_length_3=len(Configuration_3[0])
y_length_3=len(Configuration_3)

# set action function to calculate the robot operation
def robot_action_Configuration(step,Configuration,x_length,y_length):

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

            # add new move formula containing "w" and the its using precondition   
            if robot_x-target_x >= x_length/2:
                robot_action_Configuration.append("r"*(x_length - robot_x)+"w" + target_x*"r")
    
            # if new moving steps is not close enough, take original moving rule
            else:
                robot_action_Configuration.append("l"*(robot_x-target_x))

        # same logic to add new move formula containing "w" and original moving rule
        elif robot_x < target_x:
            if target_x-robot_x >= x_length/2:
                robot_action_Configuration.append("l"*(robot_x+1)+"w"+(x_length-target_x-1)*"l")
            else:
                robot_action_Configuration.append("r"*(target_x-robot_x))

        # same logic to add new move formula containing "w" and original moving rule
        if robot_y < target_y:
            if target_y-robot_y >= y_length/2:
                robot_action_Configuration.append("u"*(robot_y+1)+"w"+"u"*(y_length-target_y-1))
            else:
                robot_action_Configuration.append("d"*(target_y-robot_y))

        # same logic to add new move formula containing "w" and original moving rule
        elif robot_y > target_y:
            if robot_y-target_y >= y_length/2:
                robot_action_Configuration.append("d"*(y_length-robot_y)+"w"+"d"*target_y)
            else:
                robot_action_Configuration.append("u"*(robot_y-target_y))
        
        # when robot reaches the target coordinate, press "p"
        robot_x,robot_y=target_x,target_y
        robot_action_Configuration.append("p")

    # turn robot action list into string after the loop
    return "".join(robot_action_Configuration)

# reintroduce action function and get robot actions about four different Configurations
robot_action_0=robot_action_Configuration(string,Configuration_0,x_length_0,y_length_0)
robot_action_1=robot_action_Configuration(string,Configuration_1,x_length_1,y_length_1)
robot_action_2=robot_action_Configuration(string,Configuration_2,x_length_2,y_length_2)
robot_action_3=robot_action_Configuration(string,Configuration_3,x_length_3,y_length_3)

# remove all "" string and recalculate the robot steps length for each Configuration
length_robot_0=len(robot_action_0.replace("w",""))
length_robot_1=len(robot_action_1.replace("w",""))
length_robot_2=len(robot_action_2.replace("w",""))
length_robot_3=len(robot_action_3.replace("w",""))

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

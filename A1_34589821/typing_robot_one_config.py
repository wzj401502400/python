"""
This is a login program which commands robot 
to outcome the string by moving operation and
output the action steps.
"""

# get the string
string=input("Enter a string to type: ")

# list the string keyboard
string_keyboard=["abcdefghijklm",
                 "nopqrstuvwxyz"]

# set a function to define string position
def string_position(x):
    
    # y means every possible rows, x means appearing position in the row   
    for y in range(len(string_keyboard)):
        if x in string_keyboard[y]:
            
            # return position
            return(string_keyboard[y].index(x),y)
            
    # quit the program if it contains unknown information
    if x not in string_keyboard:
        print("The string cannot be typed out.")
        quit()

# set another function to define robot operation
def robot_action(step):

    # set a robot original coordinates 
    robot_x,robot_y=0,0

    # create an empty robot action list
    robot_action=[]

    # set loop to get coordinates by string position function
    for step in string:
        target_position=string_position(step)

        # set coordinate for target position
        target_x,target_y=target_position
                           
        # left, right, down, up, moving rules depend on specific condition
        if robot_x > target_x:
            robot_action.append("l"*(robot_x-target_x))

        elif robot_x < target_x:
            robot_action.append("r"*(target_x-robot_x))

        if robot_y < target_y:
            robot_action.append("d"*(target_y-robot_y))

        elif robot_y > target_y:
            robot_action.append("u"*(robot_y-target_y))

        # when robot reaches the target coordinate, press "p"
        robot_x,robot_y=target_x,target_y
        robot_action.append('p')

    # turn robot action list into string after the loop
    return "".join(robot_action)

# get the robot operation by action function
robot_action = robot_action(string)

# output the robot operations
print("The robot must perform the following operations:")
print(robot_action)

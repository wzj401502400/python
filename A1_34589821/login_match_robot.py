"""
This is a login program which needs a pair of right username
and passwords to verify.
"""

# a combination list to store many pairs of relative usernames and passwords
combination=[["Ava","12345"],["Leo","abcde"],["Raj","pass1"],["Zoe","qwert"],
             ["Max","aaaaa"],["Sam","zzzzz"],["Eli","11111"],["Mia","apple"],
             ["Ian","hello"],["Kim","admin"]]

# get the combination of username and password
username=input("Enter username: ")
password=input("Enter password: ")
answer_combination=[username,password]

# three chances to verify if combination belongs to the composition
tries_left = 3
robot_answer = 0

# if combination answer fails once, lose one chance and need to retype information
while answer_combination not in combination:
    print("Login incorrect.","Tries left:",tries_left-1)
    username=input("Enter username: ")
    password=input("Enter password: ") 
    answer_combination=[username,password]
    tries_left -= 1
    
    # set an extra method to verify the last chance    
    if tries_left == 1:
        while answer_combination in combination:
            print("Login successful.","Welcome",username,"!")
            quit()
        print("Login incorrect. Tries left:",tries_left-1) 

        # if there is no tries left, ask if user is robot
        while robot_answer != "Y" or "n":
            robot_answer=input("Are you a robot (Y/n)? ") 
            
            # if answer yes or empty, quit the program
            if robot_answer == "Y" or robot_answer == "":
                quit()

            # if answer is n, give three more chances to retype information
            elif robot_answer == "n":
                tries_left=3             
                username=input("Enter username: ")
                password=input("Enter password: ") 
                answer_combination=[username,password]

                # back to check loop
                break

# login successful
print("Login successful.","Welcome",username,"!")

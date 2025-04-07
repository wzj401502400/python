"""
This is a login program which needs one of right username 
and one of right passwords to verify.
"""

# create two lists about username and password
usernames_list=["Ava","Leo","Raj","Zoe","Max",
                "Sam","Eli","Mia","Ian","Kim"]

password_list=["12345","abcde","pass1","qwert","aaaaa",
               "zzzzz","11111","apple","hello","admin"]

# get the username and password
username=input("Enter username: ")
password=input("Enter password: ")

# set three chances to input username and password
left_chance = 3

# set a loop, three chances for tring if both belong to the list
while username not in usernames_list or password not in password_list:
    print("Login incorrect.","Tries left:",left_chance-1)
    username=input("Enter username: ")
    password=input("Enter password: ") 
    left_chance -= 1

    # set an extra condition for the last chance
    if left_chance == 1:

        # check username and password, if still wrong, quit the program  
        while username not in usernames_list or password not in password_list:
            print("Login incorrect. Tries left: 0")
            quit()
            
# login successful
print("Login successful.","Welcome",username,"!")



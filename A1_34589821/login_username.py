"""
This is a login program which needs right username to verify.
"""

# create a list of all names 
usernames_list=["Ava","Leo","Raj","Zoe","Max",
                "Sam","Eli","Mia","Ian","Kim"]

# get the username
username=input("Enter username: ")

# retype username until it belongs to the list
while username not in usernames_list:
    print("Login incorrect.")
    username=input("Enter username: ")

# login successful
print("Login successful.","Welcome",username,"!")


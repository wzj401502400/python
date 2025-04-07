"""
This is a program which transforms time into hours, minutes and seconds.
"""

#get the seconds
print("TIME ON EARTH")
print("Input a time in seconds:")
seconds=int(input())

# calculate minutes and remain seconds
minutes=seconds//60

remain_seconds=seconds%60

# calculate hours and remain_minutes
hours=minutes//60

remain_minutes=minutes%60

# print outcome
print("")
print("The time on Earth is",hours,"hours",remain_minutes,"minutes","and",remain_seconds,"seconds.")

"""
This is a program which transforms time into hours, minutes 
and seconds by customize rule.
"""

print("")
print("TIME ON TRISOLARIS")

# insert new calculate rule about transformation
print("Input the number of seconds in a minute on Trisolaris:")
calculate_seconds=int(input())

print("Input the number of minutes in an hour on Trisolaris:")
calculate_minutes=int(input())

# calculate time information by formula
minutes_Task2=seconds//calculate_seconds

remian_seconds_Task2=seconds%calculate_seconds

hours_Task2=minutes_Task2//calculate_minutes

remain_minutes_Task2=minutes_Task2%calculate_minutes

# print outcome
print("")
print("The time on Trisolaris is",hours_Task2,"hours",remain_minutes_Task2,"minutes","and",remian_seconds_Task2,"seconds.")

"""
This is a program which pluses two times to transforms total time into hours,
minutes and seconds by customize rulecustomize rule.
"""

print("")
print("TIME AFTER WAITING ON TRISOLARIS")
print("Input a duration in seconds:")

# adding an extra time to get total seconds

adding_time=int(input())
total_seconds=adding_time+seconds

# reintroduced the formula appearing in Task2
minutes_Task2=total_seconds//calculate_seconds

remian_seconds_Task2=total_seconds%calculate_seconds

hours_Task2=minutes_Task2//calculate_minutes

remain_minutes_Task2=minutes_Task2%calculate_minutes

# output the outcome
print("")
print("The time on Trisolaris after waiting is",hours_Task2,"hours",remain_minutes_Task2,"minutes","and",remian_seconds_Task2,"seconds.")


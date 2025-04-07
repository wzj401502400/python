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

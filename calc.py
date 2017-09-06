"""
Zachary Bedrosian
Python3 Calculater
9.6.2017
"""

"""How many seconds are there in 42 minutes 42 seconds?"""
# Convert the minutes to seconds then add them back to the remaining minutes
seconds = ((42*60) + 42)
print(seconds)

"""How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile."""
miles = (10 / 1.61)
print(miles)

"""If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace 
(time per mile in minutes and seconds)? What is your average speed in miles per hour?"""
# Determine the total number of seconds it took per mile
seconds_per_mile = (seconds / miles)

# Convert into minutes
minutes_per_mile = (seconds_per_mile/60)

# Determine the remaing seconds (in % not actual seconds)
remaining_seconds = minutes_per_mile % 1

# Get the actual number of minutes
minutes_per_mile = minutes_per_mile - remaining_seconds

# Convert the percentage of seconds into actual 60 base seconds
remaining_seconds = remaining_seconds * 60

print(str(int(minutes_per_mile)) + ":" + str(int(remaining_seconds)))

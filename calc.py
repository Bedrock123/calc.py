"""
Zachary Bedrosian
Python3 Calculater
9.6.2017

Quick Note - I am logged into my WORK github account on my local machine so all commits are done from Kingwilly
and not Bedrock123 (which is my personal repo). I can talk to you in person if you would like more clarification.
"""

import math

"""
How many seconds are there in 42 minutes 42 seconds?
"""
# Convert the minutes to seconds then add them back to the remaining minutes
seconds = ((42 * 60) + 42)
print(seconds)

"""
How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
"""
miles = (10 / 1.61)
print(miles)

"""
If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace 
(time per mile in minutes and seconds)? What is your average speed in miles per hour?
"""
# Determine the total number of seconds it took per mile
seconds_per_mile = (seconds / miles)

# Convert into minutes
minutes_per_mile = (seconds_per_mile / 60)

# Determine the remaing seconds (in % not actual seconds)
remaining_seconds = minutes_per_mile % 1

# Get the actual number of minutes
minutes_per_mile = minutes_per_mile - remaining_seconds

# Convert the percentage of seconds into actual 60 base seconds
remaining_seconds = remaining_seconds * 60

print(str(int(minutes_per_mile)) + ":" + str(int(remaining_seconds)))

"""
The volume of a sphere with radius r is (4/3)πr3. What is the volume of a sphere with radius 5?
"""
def circle_volume(radius):
    volume = ((4/3) * math.pi * radius * 3)
    return volume

print(circle_volume(5))

"""
Suppose the cover price of a book is $24.95, but bookstores get a 40\% discount.
Shipping costs $3 for the first copy and 75 cents for each additional copy.\
What is the total wholesale cost for 60 copies?
"""

# Define constants
book_price = 24.95
book_store_discount = 0.40
initial_shipping_cost = 3
additional_shipping_cost = 0.75

def total_wholesale_cost(number_of_books):

    # get base book price into total cost
    total_cost = number_of_books * book_price

    # Take in the discount
    total_cost = total_cost * (1-book_store_discount)

    # Subract out first book to caluclate additional shipping cost
    number_of_books -= 1

    total_cost += (additional_shipping_cost*number_of_books)

    # Add in the initial shipping cost
    total_cost += initial_shipping_cost

    # Round to pennies
    return round(total_cost, 2)

print(total_wholesale_cost(60))


"""
If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo
(7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
"""

# Define constants
easy_pace_in_seconds = (8 * 60) + 15
tempo_in_seconds = (7 * 60) + 12
starting_time_hour = 6
starting_time_minute = 52

# Get the total number of seconds ran
total_seconds_run = (easy_pace_in_seconds) + (3 * tempo_in_seconds) + easy_pace_in_seconds

# Convert into minute format
total_minutes_run = total_seconds_run / 60

# Add on the starting minutes with to toal minutes run
ending_time_minute = starting_time_minute + total_minutes_run

# Convert into hour format
ending_time_minute = ending_time_minute / 60

remaining_ending_time_minute = ending_time_minute

ending_time_minute = ending_time_minute % 1

ending_time_minute = ending_time_minute * 60

ending_time_hour = starting_time_hour + (remaining_ending_time_minute - (remaining_ending_time_minute % 1))

# Print out final time
print(str(int(ending_time_hour)) + ":" + str(int(ending_time_minute)))

"""
If my average grade rises from 82 to 89. What is the percentage of the increase? Format the result as 'xx.x%'.
Keep one figure after decimal point.
"""

percentage_increase = (89/82)
percentage_increase -= 1
percentage_increase *= 100

print(str(round(percentage_increase,1)) + '%')
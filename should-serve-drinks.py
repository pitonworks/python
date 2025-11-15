"""
Assignment
In Fantasy Quest, players can go to a town's local pub. Drinking virtual beer refills their stamina!

Complete the function that determines if a bartender should serve drinks to a customer. Only return True if all of these conditions apply. If any of these conditions are False, return False:

The customer's age is 21 or older
The bartender is working
The time is between 5 and 10 o'clock (inclusive)
"""

def should_serve_customer(customer_age, on_break, time):
    if customer_age >= 21 and not on_break and 5 <= time <= 10:
        return True
    else:
        return False
print(should_serve_customer(25, False, 8))  # Expected: True
print(should_serve_customer(20, False, 8))  # Expected: False

"""
Assignment
Complete the player_status function. If the player's health is less than or equal to 0, return the string:

dead

Otherwise, if it's less than or equal to 5 return the string:

injured

Otherwise, return the string:

healthy
"""

def player_status(health):
    if health <= 0:
        return "dead"
    elif health <= 5:
        return "injured"
    else:
        return "healthy"
print(player_status(20))    

# If-Else Practice
def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name == high_scoring_player_name:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"
print(check_high_score("Alice", "Bob"))  # Output: You are not the highest scoring player!
print(check_high_score("Charlie", "Charlie"))  # Output: You are the highest scoring


# if-else practice 2
"""
Assignment
Complete the check_high_score function. If the player_name matches the high score name, return the string:

high

Otherwise, if it's the low scorer, return the string:

low

Otherwise, return the string:

neither
"""
def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if player_name == high_scoring_player_name:
        return "high"
    elif player_name == low_scoring_player_name:
        return "low"
    else:
        return "neither"
print(check_high_score("Alice", "Bob", "Charlie"))  # Output: neither

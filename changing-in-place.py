"""
Assignment
Complete the update_player_score function. It should add increment to current_score and then return the new current_score.
"""

def update_player_score(current_score, increment):
    new_score = current_score + increment
    return new_score
print(update_player_score(1500, 300))
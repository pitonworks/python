"""
Boolean Logic
The operators:

< "less than"
> "greater than"
<= "less than or equal to"
>= "greater than or equal to"
== "equal to"
!= "not equal to"

Assignment
Complete the player_1_wins function. It should return True if player 1 has a higher score, and False otherwise.
"""

def player_1_wins(player_1_score, player_2_score):
    return player_1_score > player_2_score
print(player_1_wins(10, 5))  # True
print(player_1_wins(3, 7))   # False

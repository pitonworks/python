"""
Assignment
Create the following variables. Use comparison operators to determine their boolean values. The context of the parameter names should tell you how to make these comparisons. Return them in this order:

is_mustang_edward_same
is_alphonse_edward_same
is_winry_alphonse_same
"""


def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = mustang_height == edward_height
    is_alphonse_edward_same = alphonse_height == edward_height
    is_winry_alphonse_same = winry_height == alphonse_height
    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same
print(compare_heights(172, 168, 165, 172))

# Practice
"""
Assignment
Complete the can_withstand_blow function. It should return True if the hero's armor is greater than or equal to the damage dealt by the enemy, and False otherwise.
"""
def can_withstand_blow(hero_armor, enemy_damage):
    return hero_armor >= enemy_damage
print(can_withstand_blow(50, 40))  # True


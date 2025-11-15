"""
Assignment
Complete the get_hurt function. It should use the -= in-place operator to subtract damage from current_health and then return the new current_health.
"""
def get_hurt(current_health, damage):
    current_health -= damage
    return current_health
print(get_hurt(100, 30))

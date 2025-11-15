""" 
Assignment
Complete the missing sections of the calculate_damage function.

Fix the total_damage variable so that it contains the sum of all the different weapons' and spells' damage values.
Fix the average_damage variable so that it contains the average of the combined weapon and spell damage.


"""




def calculate_damage(sword, arrow, spear, dagger, fireball):
    total_damage = sword + arrow + spear + dagger + fireball
    average_damage = total_damage / 5
    return total_damage, average_damage
print(calculate_damage(50, 30, 40, 20, 60))

print(11//2) # should be 5
print(11/2)  # should be 5.5
print(11%2)  # should be 1
print(2**3)  # should be 8
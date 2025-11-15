"""
Assignment
Complete the print_status function.

If player_health is less than or equal to 0, print the text dead to the console.
Afterwards, whether or not the player is dead, print the text status check complete to the console.
"""

def print_status(player_health):
    if player_health <= 0:
        print("dead")
    print("status check complete")



def test(health):
    print(f"Player Health: {health}")
    print("Checking status...")
    print_status(health)
    print("=====================================")


def main():
    test(0)
    test(5)
    test(-1)
    test(3)


main()


# if practice
"""
Assignment
Complete the check_swords_for_army function. If the number of swords and the number of soldiers match, return the string:

correct amount

Otherwise, return the string:

incorrect amount

Punctuation matters! Make sure you return the strings exactly as they appear above.
"""
def check_swords_for_army(number_of_swords, number_of_soldiers):
    if number_of_swords == number_of_soldiers:
        return "correct amount"
    else:
        return "incorrect amount"
    
print(check_swords_for_army(10, 10))  # Output: correct amount
print(check_swords_for_army(5, 10))   # Output: incorrect amount

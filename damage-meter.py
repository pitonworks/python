"""
Assignment
Fix the interns' syntax error. The calculate_dps function should accept two arguments, but due to a syntax error, it's being called with 4 instead. Use the proper delimiter for thousands so that the numbers are still easy to parse visually.

The two numbers should be:

damage: 8 million, time: 45
damage: 10 million, time: 49
def main():
    calculate_dps(8, 000, 000, 45)
    calculate_dps(10, 000, 000, 49)

"""

def main():
    calculate_dps(8000000, 45)
    calculate_dps(10000000, 49)


# Don't edit below this line


def calculate_dps(damage, time):
    dps = damage / time
    print(f"Damage per second: {dps}")
    print("=====================================")


main()

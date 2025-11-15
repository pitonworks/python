"""
Assignment
Complete each of the get_XXX_bits functions. Simply use the bitwise & operation on the input of the user's permission bits and the appropriate guild permission bits variable, and return the resulting bits for them to be checked by the tests.

4 values have been provided, use the appropriate one for each function:

can_create_guild
can_review_guild
can_delete_guild
can_edit_guild
"""

can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001
"""
0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1
"""

def get_create_bits(user_permissions):
    permission = user_permissions & can_create_guild
    return permission


def get_review_bits(user_permissions):
    return user_permissions & can_review_guild


def get_delete_bits(user_permissions):
    return user_permissions & can_delete_guild


def get_edit_bits(user_permissions):
    return user_permissions & can_edit_guild
print(get_edit_bits(0b1010))  # Output: 0b1000

# Bitwise “|” Operator
"""
0 | 0 = 0
0 | 1 = 1
1 | 0 = 1
1 | 1 = 1
"""
def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    return glorfindel | galadriel | elendil | elrond
print(calculate_guild_perms(0b1001, 0b0110, 0b0011, 0b1110))  # Output: 0b1111

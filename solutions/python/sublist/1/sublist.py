"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one, list_two):
    # if list_one and not list_two:list_one.append([])
    # elif list_two and not list_one:list_two.append([])
    list_one=','.join(map(str,list_one))+','
    list_two=','.join(map(str,list_two))+','
    if list_one==list_two: return 2
    elif list_one in list_two: return 0
    elif list_two in list_one: return 1
    else: return 3

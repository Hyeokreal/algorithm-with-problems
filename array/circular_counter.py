"""
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.

For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271
"""

a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def circular(int_list, skip):
    i = 1
    point = 0
    while len(a):
        if point >= len(a):
            point = 0
        if not i % skip:
            print(int_list.pop(point), end="")
            point -= 1
        i += 1
        point += 1



def josepheus(int_list, skip):
    skip = skip - 1  # list starts with 0 index
    idx = 0
    while len(int_list):
        idx = (skip + idx) % len(
            int_list)  # hashing to keep changing the index to every 3rd
        print(int_list.pop(idx))


circular(a, 3)
josepheus(a, 3)

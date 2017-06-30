"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
give a single resultant array.

function flatten(input){
}

Example:

Input: var input = [2, 1, [3, [4, 5], 6], 7, [8]];
flatten(input);
Output: [2, 1, 3, 4, 5, 6, 7, 8]
"""

result = []

def flatten(l):
    if len(l):
        if isinstance(l[0], int):
            result.append(l.pop(0))
            flatten(l)
        elif isinstance(l[0], list):
            l2 = l[0] + l[1:]
            flatten(l2)

input_list = [2, [1, [3, [4, 5], 6], 7], [8]]

flatten(input_list)
print(result)





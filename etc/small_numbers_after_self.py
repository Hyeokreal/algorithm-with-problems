"""
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller
elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
"""


def count_smaller_bad_way(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    max_index = len(nums)

    counts = []

    for i in range(max_index):
        count = 0
        for j in range(i, max_index):
            if nums[i] > nums[j]:
                count += 1
        counts.append(count)

    return counts

def count_smaller(nums):
    def sort(enum):
        half = len(enum) / 2
        if half:
            left, right = sort(enum[:half]), sort(enum[half:])
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum
    smaller = [0] * len(nums)
    sort(list(enumerate(nums)))
    return smaller


input_num = [5, 2, 6, 1]

print(count_smaller(input_num))
print(count_smaller_bad_way(input_num))
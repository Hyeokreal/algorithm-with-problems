"""
Given an array of integers, return indices of the two numbers such that
they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def two_sum_bad_way(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    sorted_nums = sorted(nums)
    front = 0
    end = len(nums) - 1

    for i in reversed(sorted_nums):
        if i >= target:
            end -= 1
        else:
            break

    while True:
        pair_sum = sorted_nums[front] + sorted_nums[end]
        if pair_sum < target:
            front += 1
        elif pair_sum > target:
            end -= 1
        else:
            break

    front_val = sorted_nums[front]
    end_val = sorted_nums[end]
    origin_front = nums.index(front_val)

    if front_val == end_val:
        origin_end = nums.index(end_val, origin_front + 1)
    else:
        origin_end = nums.index(end_val)

    if origin_front > origin_end:
        return [origin_end, origin_front]

    return [origin_front, origin_end]


def two_sum(nums: "List[int]", target: "int") -> "List[int]":
    dic = {}
    for i, num in enumerate(nums):
        print("i: ", i, " num : ", num)

        if num in dic:
            return [dic[num], i]
        else:
            dic[target - num] = i
        print(dic)


input_nums = [2, 5, 5, 11]
target = 10

print(two_sum(input_nums, target))
print(two_sum_bad_way(input_nums, target))

"""
What i learned
"""

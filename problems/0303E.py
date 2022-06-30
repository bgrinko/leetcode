"""LeetCode problem 303. Range Sum Query - Immutable

Link:       https://leetcode.com/problems/range-sum-query-immutable/
Difficulty: Easy
Status:     Accepted (06/30/2022 23:10) 1104 ms 17.4 MB
"""


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])

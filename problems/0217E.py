"""LeetCode problem 217. Contains Duplicate

Link:       https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Status:     Accepted (01/23/2022 05:28) 475 ms 25.9 MB
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

"""LeetCode problem 268. Missing Number

Link:       https://leetcode.com/problems/missing-number/
Difficulty: Easy
Status:     Accepted (07/06/2022 21:18) 140 ms 15.1 MB
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i in range(result - 1, -1, -1):
            result += i - nums[i]
        return result

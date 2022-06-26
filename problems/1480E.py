"""LeetCode problem 1480. Running Sum of 1d Array

Link:       https://leetcode.com/problems/running-sum-of-1d-array/
Difficulty: Easy
Status:     Accepted (06/26/2022 19:15) 50 ms 14.2 MB
"""


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(1, nums.__len__() + 1):
            ans.append(sum(nums[0:i]))
        return ans

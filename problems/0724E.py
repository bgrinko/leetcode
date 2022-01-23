"""LeetCode problem 724. Find Pivot Index

Link:       https://leetcode.com/problems/find-pivot-index/
Difficulty: Easy
Status:     Accepted (01/22/2022 01:15) 144 ms 15.3 MB
"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_l = 0
        sum_r = sum(nums)

        for i in range(len(nums)):
            sum_r -= nums[i]
            if sum_l == sum_r:
                return i
            sum_l += nums[i]

        return -1

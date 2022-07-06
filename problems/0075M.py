"""LeetCode problem 75. Sort Colors

Link:       https://leetcode.com/problems/sort-colors/
Difficulty: Medium
Status:     Accepted (07/06/2022 21:02) 60 ms 13.8 MB
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        d = [0] * 3
        for i in nums:
            d[i] += 1
        p = 0
        for e, i in enumerate(d):
            for j in range(i):
                nums[p] = e
                p += 1

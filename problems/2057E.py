"""LeetCode problem 2057. Smallest Index With Equal Value

Link:       https://leetcode.com/problems/smallest-index-with-equal-value/
Difficulty: Easy
Status:     Accepted (07/02/2022 13:06) 84 ms 13.8 MB
"""


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for k, v in enumerate(nums):
            if k % 10 == v:
                return k
        return -1

"""LeetCode problem 1464. Maximum Product of Two Elements in an Array

Link:       https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
Difficulty: Easy
Status:     Accepted (06/27/2022 02:57) 873 ms 14 MB
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = 0
        for k, v in enumerate(nums):
            for i, j in enumerate(nums):
                if k != i and m < (v - 1) * (j - 1):
                    m = (v - 1) * (j - 1)
        return m

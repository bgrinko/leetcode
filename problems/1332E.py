"""LeetCode problem 1332. Remove Palindromic Subsequences

Link:       https://leetcode.com/problems/remove-palindromic-subsequences/
Difficulty: Easy
Status:     Accepted (06/30/2022 21:49) 52 ms 13.9 MB
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[i + m] = nums2[i]
        nums1.sort()

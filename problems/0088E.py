"""LeetCode problem 88. Merge Sorted Array

Link:       https://leetcode.com/problems/merge-sorted-array/
Difficulty: Easy
Status:     Accepted (06/30/2022 21:40) 45 ms 13.9 MB
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[i + m] = nums2[i]
        nums1.sort()

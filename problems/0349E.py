"""LeetCode problem 349. Intersection of Two Arrays

Link:       https://leetcode.com/problems/intersection-of-two-arrays/
Difficulty: Easy
Status:     Accepted (07/08/2022 01:37) 68 ms 13.9 MB
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(nums2))

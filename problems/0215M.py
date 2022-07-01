"""LeetCode problem 215. Kth Largest Element in an Array

Link:       https://leetcode.com/problems/kth-largest-element-in-an-array/
Difficulty: Medium
Status:     Accepted (07/01/2022 12:42) 82 ms 14.6 MB
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]

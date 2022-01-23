"""LeetCode problem 26. Remove Duplicates from Sorted Array

Link:       https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Difficulty: Easy
Status:     Accepted (01/22/2022 12:21) 112 ms 15.6 MB
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p, k = 0, None
        for i in range(len(nums)):
            if k != nums[i]:
                nums[p] = nums[i]
                k = nums[i]
                p += 1
        return p

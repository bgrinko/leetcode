"""LeetCode problem 704. Binary Search

Link:       https://leetcode.com/problems/binary-search/
Difficulty: Easy
Status:     Accepted (01/23/2022 03:01) 288 ms 15.6 MB
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            k = l + (r - l) // 2
            if nums[k] == target:
                return k
            if target < nums[k]:
                r = k - 1
            else:
                l = k + 1
        return -1

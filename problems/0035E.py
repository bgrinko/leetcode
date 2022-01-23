"""LeetCode problem 35. Search Insert Position

Link:       https://leetcode.com/problems/search-insert-position/
Difficulty: Easy
Status:     Accepted (01/23/2022 04:27) 59 ms 15.1 MB
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
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

        return l

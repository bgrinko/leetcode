"""LeetCode problem 27. Remove Element

Link:       https://leetcode.com/problems/remove-element/
Difficulty: Easy
Status:     Accepted (01/22/2022 14:37) 36 ms 14.1 MB
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pos] = nums[i]
                pos += 1
        return pos

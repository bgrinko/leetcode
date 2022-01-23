"""LeetCode problem 283. Move Zeroes

Link:       https://leetcode.com/problems/move-zeroes/
Difficulty: Easy
Status:     Accepted (01/23/2022 03:58) 175 ms 15.4 MB
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 0

        while i <= len(nums) - 1:
            if nums[i] == 0:
                nums.pop(i)
                j += 1
            else:
                i += 1

        nums += j * [0]

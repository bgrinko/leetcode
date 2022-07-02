"""LeetCode problem 2293. Min Max Game

Link:       https://leetcode.com/problems/min-max-game/
Difficulty: Easy
Status:     Accepted (07/02/2022 12:02) 97 ms 14.1 MB
"""


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            new = [0] * (len(nums) // 2)
            for i in range(len(nums) // 2):
                if i % 2 == 0:
                    new[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    new[i] = max(nums[2 * i], nums[2 * i + 1])
            nums = new
        return nums[0]

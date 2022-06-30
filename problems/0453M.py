"""LeetCode problem 453. Minimum Moves to Equal Array Elements

Link:       https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
Difficulty: Medium
Status:     Accepted (06/30/2022 21:16) 573 ms 15.5 MB
"""


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        mi, result = nums[0], 0
        for i in range(len(nums) - 1, -1, -1):
            result += (result + nums[i] - mi)
            mi = nums[0] + result
        return result

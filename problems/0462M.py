"""LeetCode problem 462. Minimum Moves to Equal Array Elements II

Link:       https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
Difficulty: Medium
Status:     Accepted (06/30/2022 20:31) 81 ms 15.3 MB
"""


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        k = nums[len(nums) // 2]
        return sum(abs(k - i) for i in nums)

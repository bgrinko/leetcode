"""LeetCode problem 46. Permutations

Link:       https://leetcode.com/problems/permutations/
Difficulty: Medium
Status:     Accepted (06/28/2022 22:32) 65 ms 14 MB
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))

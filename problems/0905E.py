"""LeetCode problem 905. Sort Array By Parity

Link:       https://leetcode.com/problems/sort-array-by-parity/
Difficulty: Easy
Status:     Accepted (06/28/2022 17:11) 153 ms 14.6 MB
"""


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda val: val % 2 != 0)
        return nums

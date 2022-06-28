"""LeetCode problem 561. Array Partition I

Link:       https://leetcode.com/problems/array-partition-i/
Difficulty: Easy
Status:     Accepted (06/28/2022 17:01) 523 ms 16.8 MB
"""


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum([v if k % 2 == 0 else 0 for k, v in enumerate(nums)])

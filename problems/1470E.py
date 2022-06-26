"""LeetCode problem 1470. Shuffle the Array

Link:       https://leetcode.com/problems/shuffle-the-array/
Difficulty: Easy
Status:     Accepted (06/26/2022 20:03) 112 ms 14.1 MB
"""


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result

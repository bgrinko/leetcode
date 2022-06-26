"""LeetCode problem 1365. How Many Numbers Are Smaller Than the Current Number

Link:       https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
Difficulty: Easy
Status:     Accepted (06/26/2022 21:03) 542 ms 14 MB
"""


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = [0] * nums.__len__()
        for i, n in enumerate(nums):
            for k in nums:
                if k < n:
                    result[i] += 1

        return result

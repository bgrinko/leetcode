"""LeetCode problem 1979. Find Greatest Common Divisor of Array

Link:       https://leetcode.com/problems/find-greatest-common-divisor-of-array/
Difficulty: Easy
Status:     Accepted (07/02/2022 12:52) 61 ms 14 MB
"""


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        ma = max(nums)
        mi = min(nums)
        result = 1
        for i in range(1, mi + 1):
            if ma % i == 0 and mi % i == 0:
                result = i
        return result

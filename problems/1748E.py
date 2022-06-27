"""LeetCode problem 1748. Sum of Unique Elements

Link:       https://leetcode.com/problems/sum-of-unique-elements/
Difficulty: Easy
Status:     Accepted (06/27/2022 03:20) 33 ms 13.9 MB
"""


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        result = 0

        for k, v in d.items():
            if v == 1:
                result += k

        return result

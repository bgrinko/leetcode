"""LeetCode problem 2169. Count Operations to Obtain Zero

Link:       https://leetcode.com/problems/count-operations-to-obtain-zero/
Difficulty: Easy
Status:     Accepted (07/02/2022 01:14) 119 ms 13.8 MB
"""


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        c = 0
        while True:
            if num1 == 0 or num2 == 0:
                return c
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            c += 1

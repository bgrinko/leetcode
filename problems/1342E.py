"""LeetCode problem 1342. Number of Steps to Reduce a Number to Zero

Link:       https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
Difficulty: Easy
Status:     Accepted (06/26/2022 20:44) 51 ms 13.9 MB
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        c = 0

        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
            c += 1

        return c

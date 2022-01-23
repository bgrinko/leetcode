"""LeetCode problem 258. Add Digits

Link:       https://leetcode.com/problems/add-digits/
Difficulty: Easy
Status:     Accepted (01/22/2022 21:49) 45 ms 13.8 MB
"""


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return num
        num = num % 9
        if num == 0:
            num = 9
        return num

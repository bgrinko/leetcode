"""LeetCode problem 1221. Split a String in Balanced Strings

Link:       https://leetcode.com/problems/split-a-string-in-balanced-strings/
Difficulty: Easy
Status:     Accepted (07/04/2022 23:40) 37 ms 13.9 MB
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        z = 0
        result = 0
        for i in s:
            if i == 'L':
                z += 1
            else:
                z -= 1
            if z == 0:
                result += 1

        return result

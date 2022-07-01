"""LeetCode problem 13. Roman to Integer

Link:       https://leetcode.com/problems/roman-to-integer/
Difficulty: Easy
Status:     Accepted (07/01/2022 17:22) 60 ms 13.9 MB
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result, i = 0, 0

        while i < len(s):
            q = d[s[i]]
            if i + 1 < len(s):
                w = d[s[i + 1]]
                if q >= w:
                    result += q
                else:
                    result -= q
            else:
                result += q
            i += 1

        return result

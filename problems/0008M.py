"""LeetCode problem 8. String to Integer (atoi)

Link:       https://leetcode.com/problems/string-to-integer-atoi/
Difficulty: Medium
Status:     Accepted (01/25/2022 01:23) 39 ms 14.2 MB
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        result = ""

        ma, mi = 2 ** 31 - 1, -2 ** 31

        if s and s[0] in ['+', '-']:
            result, s = s[0], s[1:]

        for i in s:
            if i.isnumeric():
                result += i
            else:
                break

        if result in ['+', '-'] or not result:
            return 0

        result = int(result)

        if result > ma:
            return ma
        if result < mi:
            return mi

        return result

"""LeetCode problem 7. Reverse Integer

Link:       https://leetcode.com/problems/reverse-integer/
Difficulty: Medium
Status:     Accepted (07/05/2022 21:54) 74 ms 13.9 MB
"""


class Solution:
    def reverse(self, x: int) -> int:
        mx, mi = 2 ** 31 - 1, -2 ** 31

        result = 0

        sign = True
        if x < 0:
            x = -x
            sign = False

        while x != 0:
            j = x % 10
            x //= 10
            result = result * 10 + j

        if not sign:
            result = -result

        if result > mx:
            return 0
        elif result < mi:
            return 0
        else:
            return result

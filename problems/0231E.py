"""LeetCode problem 231. Power of Two

Link:       https://leetcode.com/problems/power-of-two/
Difficulty: Easy
Status:     Accepted (06/25/2022 21:17) 66 ms 13.9 MB
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n > 0) and ((n & (n - 1)) == 0)

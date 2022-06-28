"""LeetCode problem 1837. Sum of Digits in Base K

Link:       https://leetcode.com/problems/sum-of-digits-in-base-k/
Difficulty: Easy
Status:     Accepted (06/28/2022 16:23) 56 ms 13.8 MB
"""


class Solution:
    def sumBase(self, n: int, k: int) -> int:
        r = ""
        while n > 0:
            r = str(n % k) + r
            n = n // k

        return sum(int(i) for i in r)

"""LeetCode problem 509. Fibonacci Number

Link:       https://leetcode.com/problems/fibonacci-number/
Difficulty: Easy
Status:     Accepted (07/06/2022 10:36) 1083 ms 13.8 MB
"""


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

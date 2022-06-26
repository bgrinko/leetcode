"""LeetCode problem 2011. Final Value of Variable After Performing Operations

Link:       https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
Difficulty: Easy
Status:     Accepted (06/26/2022 19:23) 44 ms 13.8 MB
"""


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        a = operations.count("X++") + operations.count("++X")
        m = operations.count("X--") + operations.count("--X")
        return a - m

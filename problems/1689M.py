"""LeetCode problem 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

Link:       https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
Difficulty: Medium
Status:     Accepted (06/27/2022 20:18) 335 ms 16.3 MB
"""


class Solution:
    def minPartitions(self, n: str) -> int:
        return max([int(i) for i in n])

"""LeetCode problem 128. Longest Consecutive Sequence

Link:       https://leetcode.com/problems/longest-consecutive-sequence/
Difficulty: Medium
Status:     Accepted (07/05/2022 03:20) 360 ms 28 MB
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        result = 0

        for i in d:
            if i - 1 not in d:
                mn = i
                cx = 1

                while mn + 1 in d:
                    mn += 1
                    cx += 1

                result = max(result, cx)

        return result

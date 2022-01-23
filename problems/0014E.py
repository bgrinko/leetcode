"""LeetCode problem 14. Longest Common Prefix

Link:       https://leetcode.com/problems/longest-common-prefix/
Difficulty: Easy
Status:     Accepted (01/22/2022 14:30) 32 ms 14.3 MB
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0]) + 1):
            if len(list(filter(lambda x: x.startswith(strs[0][0:i]), strs))) == len(strs):
                prefix = strs[0][0:i]
            else:
                break
        return prefix

"""LeetCode problem 1528. Shuffle String

Link:       https://leetcode.com/problems/shuffle-string/
Difficulty: Easy
Status:     Accepted (06/26/2022 19:58) 84 ms 14 MB
"""


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [""] * indices.__len__()
        for k, v in enumerate(indices):
            result[v] = s[k]
        return "".join(result)

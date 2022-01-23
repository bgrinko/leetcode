"""LeetCode problem 344. Reverse String

Link:       https://leetcode.com/problems/reverse-string/
Difficulty: Easy
Status:     Accepted (01/22/2022 22:06) 307 ms 18.3 MB
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]

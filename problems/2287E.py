"""LeetCode problem 2287. Rearrange Characters to Make Target String

Link:       https://leetcode.com/problems/rearrange-characters-to-make-target-string/
Difficulty: Easy
Status:     Accepted (07/01/2022 13:52) 57 ms 13.9 MB
"""


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        result = 10000
        for i in target:
            e = s.count(i)
            m = target.count(i)
            if result > e // m:
                result = e // m

        return result

"""LeetCode problem 2309. Greatest English Letter in Upper and Lower Case

Link:       https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/
Difficulty: Easy
Status:     Accepted (07/02/2022 11:55) 40 ms 13.8 MB
"""


class Solution:
    def greatestLetter(self, s: str) -> str:
        for i in string.ascii_lowercase[::-1]:
            if i in s and i.upper() in s:
                return i.upper()
        return ""

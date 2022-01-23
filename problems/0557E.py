"""LeetCode problem 557. Reverse Words in a String III

Link:       https://leetcode.com/problems/reverse-words-in-a-string-iii/
Difficulty: Easy
Status:     Accepted (01/23/2022 19:36) 55 ms 15.2 MB
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        e = s.split()
        s = ""
        for i in e:
            s += i[::-1] + " "
        return s.rstrip()
"""LeetCode problem 1945. Sum of Digits of String After Convert

Link:       https://leetcode.com/problems/sum-of-digits-of-string-after-convert/
Difficulty: Easy
Status:     Accepted (01/22/2022 22:01) 43 ms 14.3 MB
"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alf = "abcdefghijklmnopqrstuvwxyz"
        r = ""

        for i in s:
            r += str(alf.find(i) + 1)

        for i in range(k):
            r = str(sum(int(j) for j in r))

        return int(r)

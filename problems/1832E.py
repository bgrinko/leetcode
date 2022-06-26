"""LeetCode problem 1832. Check if the Sentence Is Pangram

Link:       https://leetcode.com/problems/check-if-the-sentence-is-pangram/
Difficulty: Easy
Status:     Accepted (06/27/2022 02:47) 60 ms 13.9 MB
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set("abcdefghijklmnopqrstuvwxyz")
        for i in sentence:
            if i in s:
                s.remove(i)

        return s.__len__() == 0

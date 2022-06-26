"""LeetCode problem 1859. Sorting the Sentence

Link:       https://leetcode.com/problems/sorting-the-sentence/
Difficulty: Easy
Status:     Accepted (06/27/2022 02:29) 42 ms 13.9 MB
"""


class Solution:
    def sortSentence(self, s: str) -> str:
        k = s.split()
        result = [""] * k.__len__()
        for i in k:
            result[int(i[-1]) - 1] = i[0:-1]

        return " ".join(result)

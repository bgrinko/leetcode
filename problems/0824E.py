"""LeetCode problem 824. Goat Latin

Link:       https://leetcode.com/problems/goat-latin/
Difficulty: Easy
Status:     Accepted (06/28/2022 20:52) 66 ms 13.9 MB
"""


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        lst = sentence.split()
        for i in range(len(lst)):
            if lst[i][0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                lst[i] += 'ma'
            else:
                lst[i] = lst[i][1:] + lst[i][0] + 'ma'

            lst[i] += 'a' * (i + 1)

        return " ".join(lst)

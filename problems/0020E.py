"""LeetCode problem 20. Valid Parentheses

Link:       https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy
Status:     Accepted (06/30/2022 19:58) 39 ms 13.9 MB
"""


class Solution:
    def isValid(self, s: str) -> bool:
        d, lst = {'}': '{', ']': '[', ')': '('}, []
        for i in s:
            if i in ['(', '[', '{']:
                lst.append(i)
            elif len(lst) > 0:
                l = lst.pop()
                if l != d[i]:
                    return False
            else:
                return False
        return len(lst) == 0

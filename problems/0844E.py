"""LeetCode problem 844. Backspace String Compare

Link:       https://leetcode.com/problems/backspace-string-compare/
Difficulty: Easy
Status:     Accepted (07/10/2022 23:42) 61 ms 13.8 MB
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1 = []
        for i in s:
            if i == '#':
                if st1:
                    st1.pop()
            else:
                st1.append(i)

        st2 = []
        for i in t:
            if i == '#':
                if st2:
                    st2.pop()
            else:
                st2.append(i)

        return st1 == st2

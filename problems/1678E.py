"""LeetCode problem 1678. Goal Parser Interpretation

Link:       https://leetcode.com/problems/goal-parser-interpretation/
Difficulty: Easy
Status:     Accepted (06/26/2022 20:56) 63 ms 13.9 MB
"""


class Solution:
    def interpret(self, command: str) -> str:
        k = 0
        result = ""
        while k <= command.__len__() - 1:
            if command[k] == 'G':
                result += 'G'
                k += 1
            elif command[k] == '(' and command[k + 1] == ')':
                result += 'o'
                k += 2
            else:
                result += 'al'
                k += 4
        return result

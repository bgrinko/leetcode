"""LeetCode problem 155. Min Stack

Link:       https://leetcode.com/problems/min-stack/
Difficulty: Easy
Status:     Accepted (01/22/2022 21:08) 95 ms 18.6 MB
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min = inf

    def push(self, val: int) -> None:
        if val < self.min:
            self.min = val
        self.stack.append([val, self.min])

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) == 0:
            self.min = inf
        else:
            self.min = self.stack[-1][1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

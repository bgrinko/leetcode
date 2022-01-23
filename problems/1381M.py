"""LeetCode problem 1381. Design a Stack With Increment Operation

Link:       https://leetcode.com/problems/design-a-stack-with-increment-operation/
Difficulty: Medium
Status:     Accepted (01/22/2022 05:10) 140 ms 15.2 MB
"""


class CustomStack:
    def __init__(self, maxSize: int):
        self.size = maxSize
        self.values = []

    def push(self, x: int) -> None:
        if len(self.values) == self.size:
            return
        self.values.append(x)

    def pop(self) -> int:
        if len(self.values) == 0:
            return -1
        return self.values.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.values))):
            self.values[i] += val

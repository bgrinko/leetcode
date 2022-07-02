"""LeetCode problem 295. Find Median from Data Stream

Link:       https://leetcode.com/problems/find-median-from-data-stream/
Difficulty: Hard
Status:     Accepted (07/02/2022 18:24) 2349 ms 35.9 MB
"""


class MedianFinder:
    def __init__(self):
        self.size = 0
        self.arr = []
        self.median = None

    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num)
        self.size += 1
        if self.size % 2 == 1:
            self.median = self.arr[self.size // 2]
        else:
            self.median = (self.arr[self.size // 2] + self.arr[self.size // 2 - 1]) / 2

    def findMedian(self) -> float:
        return self.median

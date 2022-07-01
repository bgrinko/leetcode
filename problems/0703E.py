"""LeetCode problem 703. Kth Largest Element in a Stream

Link:       https://leetcode.com/problems/kth-largest-element-in-a-stream/
Difficulty: Easy
Status:     Accepted (07/01/2022 16:13) 191 ms 18.2 MB
"""


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        return self.nums[-self.k]

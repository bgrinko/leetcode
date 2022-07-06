"""LeetCode problem 1089. Duplicate Zeros

Link:       https://leetcode.com/problems/duplicate-zeros/
Difficulty: Easy
Status:     Accepted (07/06/2022 23:32) 116 ms 14.8 MB
"""


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i, n = 0, len(arr)
        while i < n:
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                i += 1
                arr.pop()
            i += 1

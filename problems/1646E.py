"""LeetCode problem 1646. Get Maximum in Generated Array

Link:       https://leetcode.com/problems/get-maximum-in-generated-array/
Difficulty: Easy
Status:     Accepted (07/09/2022 23:56) 49 ms 13.8 MB
"""


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return n
        arr = [0, 1]
        for i in range(2, n + 1):
            if i % 2 == 0:
                arr.append(arr[i // 2])
            else:
                arr.append(arr[i // 2] + arr[i // 2 + 1])
        return max(arr)

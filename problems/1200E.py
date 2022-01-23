"""LeetCode problem 1200. Minimum Absolute Difference

Link:       https://leetcode.com/problems/minimum-absolute-difference/
Difficulty: Easy
Status:     Accepted (01/22/2022 05:00) 352 ms 28.1 MB
"""


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        bf = 100000000
        result = []

        for i in range(len(arr)):
            if i >= len(arr) - 1:
                break

            if arr[i + 1] - arr[i] < bf:
                bf = arr[i + 1] - arr[i]
                result = [[arr[i], arr[i + 1]]]
            elif arr[i + 1] - arr[i] == bf:
                result.append([arr[i], arr[i + 1]])

        return result

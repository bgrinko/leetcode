"""LeetCode problem 1313. Decompress Run-Length Encoded List

Link:       https://leetcode.com/problems/decompress-run-length-encoded-list/
Difficulty: Easy
Status:     Accepted (06/26/2022 20:47) 104 ms 14.3 MB
"""


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(nums.__len__() // 2):
            result += [nums[2 * i + 1]] * nums[2 * i]

        return result

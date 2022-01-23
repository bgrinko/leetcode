"""LeetCode problem 977. Squares of a Sorted Array

Link:       https://leetcode.com/problems/squares-of-a-sorted-array/
Difficulty: Easy
Status:     Accepted (01/23/2022 03:15) 425 ms 16.2 MB
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1

        result = []
        while True:
            if i == j:
                result.append(nums[i] ** 2)
                break
            if nums[i] ** 2 > nums[j] ** 2:
                result.append(nums[i] ** 2)
                i += 1
            else:
                result.append(nums[j] ** 2)
                j -= 1
        result.reverse()
        return result
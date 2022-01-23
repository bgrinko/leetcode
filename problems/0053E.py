"""LeetCode problem 53. Maximum Subarray

Link:       https://leetcode.com/problems/maximum-subarray/
Difficulty: Easy
Status:     Accepted (01/22/2022 15:21) 849 ms 28.7 MB
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        found = -1000000
        last_max = -1000000
        for i in range(len(nums)):
            if found + nums[i] < nums[i]:
                found = nums[i]
            else:
                found += nums[i]

            if last_max < found:
                last_max = found

        return last_max

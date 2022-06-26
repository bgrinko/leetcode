"""LeetCode problem 1920. Build Array from Permutation

Link:       https://leetcode.com/problems/build-array-from-permutation/
Difficulty: Easy
Status:     Accepted (06/26/2022 19:07) 225 ms 14.2 MB
"""


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0] * nums.__len__()
        for i in range(nums.__len__()):
            ans[i] = nums[nums[i]]
        return ans

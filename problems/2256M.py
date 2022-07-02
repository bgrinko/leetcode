"""LeetCode problem 2256. Minimum Average Difference

Link:       https://leetcode.com/problems/minimum-average-difference/
Difficulty: Medium
Status:     Accepted (07/02/2022 20:33) 1865 ms 25.8 MB
"""


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        pums = [0] * n
        pums[0] = nums[0]
        for i in range(1, n):
            pums[i] = pums[i - 1] + nums[i]

        mdif = inf
        result = 0
        for i in range(n):
            if n - (i + 1) == 0:
                e = abs(pums[i] // (i + 1))
            else:
                e = abs(pums[i] // (i + 1) - (pums[-1] - pums[i]) // (n - (i + 1)))
            if mdif > e:
                mdif = e
                result = i
        return result

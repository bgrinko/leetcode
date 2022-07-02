"""LeetCode problem 198. House Robber

Link:       https://leetcode.com/problems/house-robber/
Difficulty: Medium
Status:     Accepted (07/02/2022 18:13) 38 ms 13.9 MB
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        r = dict()
        mx = 0
        for k, v in enumerate(nums):
            r[k] = []
            if k - 2 >= 0:
                i = max(r[k - 2])
                r[k].append(v + i)
                if v + i > mx:
                    mx = v + i
            if k - 3 >= 0:
                i = max(r[k - 3])
                r[k].append(v + i)
                if v + i > mx:
                    mx = v + i
            if k < 2:
                r[k].append(v)
                if v > mx:
                    mx = v
        return mx

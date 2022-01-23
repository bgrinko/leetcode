"""LeetCode problem 1. Two Sum

Link:       https://leetcode.com/problems/two-sum/
Difficulty: Easy
Status:     Accepted (01/23/2022 02:29) 111 ms 16.3 MB
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dc = dict()

        for i in range(len(nums)):
            if nums[i] in dc:
                dc[nums[i]] += [i]
            else:
                dc[nums[i]] = [i]

        for k, v in dc.items():
            y = target - k
            if y in dc:
                if dc[y] == v and len(v) < 2:
                    continue
                elif dc[y] == v and len(v) > 1:
                    return [v[0], dc[y][1]]
                else:
                    return [v[0], dc[y][0]]

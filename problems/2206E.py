"""LeetCode problem 2206. Divide Array Into Equal Pairs

Link:       https://leetcode.com/problems/divide-array-into-equal-pairs/
Difficulty: Easy
Status:     Accepted (07/02/2022 13:08) 241 ms 14.1 MB
"""


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        for i in range(1, 501):
            if nums.count(i) % 2 != 0:
                return False
        return True

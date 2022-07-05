"""LeetCode problem 169. Majority Element

Link:       https://leetcode.com/problems/majority-element/
Difficulty: Easy
Status:     Accepted (07/06/2022 01:13) 255 ms 15.5 MB
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]

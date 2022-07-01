"""LeetCode problem 414. Third Maximum Number

Link:       https://leetcode.com/problems/third-maximum-number/
Difficulty: Easy
Status:     Accepted (07/01/2022 16:47) 86 ms 14.8 MB
"""


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m1, m2, m3 = -inf, -inf, -inf

        for i in nums:
            if i == m1 or i == m2 or i == m3:
                continue
            elif i > m1:
                m3 = m2
                m2 = m1
                m1 = i
            elif i > m2:
                m3 = m2
                m2 = i
            elif i > m3:
                m3 = i

        return m3 if m3 != -inf else m1


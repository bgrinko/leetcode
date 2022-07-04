"""LeetCode problem 1423. Maximum Points You Can Obtain from Cards

Link:       https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
Difficulty: Medium
Status:     Accepted (07/05/2022 00:15) 585 ms 27.5 MB
"""


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sm, l = sum(cardPoints), len(cardPoints)

        result = 0
        xm = sum(cardPoints[0:l - k])
        result = max(result, sm - xm)

        for i in range(1, k + 1):
            xm = xm - cardPoints[i - 1] + cardPoints[l - k + i - 1]
            result = max(result, sm - xm)

        return sm if l - k == 0 else result

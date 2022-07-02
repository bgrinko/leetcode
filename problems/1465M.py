"""LeetCode problem 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

Link:       https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
Difficulty: Medium
Status:     Accepted (07/02/2022 13:02) 356 ms 26.7 MB
"""


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        m1, m2 = 0, 0
        for i in range(len(horizontalCuts) - 1):
            if horizontalCuts[i + 1] - horizontalCuts[i] > m1:
                m1 = horizontalCuts[i + 1] - horizontalCuts[i]
        for i in range(len(verticalCuts) - 1):
            if verticalCuts[i + 1] - verticalCuts[i] > m2:
                m2 = verticalCuts[i + 1] - verticalCuts[i]
        return (m1 * m2) % (10 ** 9 + 7)

"""LeetCode problem 1046. Last Stone Weight

Link:       https://leetcode.com/problems/last-stone-weight/
Difficulty: Easy
Status:     Accepted (07/10/2022 00:35) 41 ms 13.8 MB
"""


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            x, y = stones[-1], stones[-2]
            if x == y:
                del stones[-1]
                del stones[-1]
            else:
                stones[-2] = stones[-1] - stones[-2]
                del stones[-1]
                stones.sort()

        return 0 if len(stones) == 0 else stones[0]

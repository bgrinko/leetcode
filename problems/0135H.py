"""LeetCode problem 135. Candy

Link:       https://leetcode.com/problems/candy/
Difficulty: Hard
Status:     Accepted (07/04/2022 08:21) 178 ms 16.8 MB
"""


class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        r1 = [1] * l
        for i in range(1, l):
            if ratings[i] > ratings[i - 1]:
                r1[i] = r1[i - 1] + 1
        r2 = [1] * l
        for i in range(l - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                r2[i] = r2[i + 1] + 1

        result = 0
        for i in range(l):
            result += max(r1[i], r2[i])

        return result

"""LeetCode problem 2320. Count Number of Ways to Place Houses

Link:       https://leetcode.com/problems/count-number-of-ways-to-place-houses/
Difficulty: Medium
Status:     Accepted (07/02/2022 19:44) 728 ms 14 MB
"""


class Solution:
    def countHousePlacements(self, n: int) -> int:
        result = [1, 4, 9]
        if n <= 2:
            return result[n]
        for i in range(3, n + 1):
            r = result[2] * 2 + result[1] * 2 - result[0]
            result[0] = result[1]
            result[1] = result[2]
            result[2] = r

        return result[2] % (10 ** 9 + 7)

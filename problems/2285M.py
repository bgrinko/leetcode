"""LeetCode problem 2285. Maximum Total Importance of Roads

Link:       https://leetcode.com/problems/maximum-total-importance-of-roads/
Difficulty: Medium
Status:     Accepted (07/02/2022 20:06) 2674 ms 42.8 MB
"""


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        r = {k: 0 for k in range(n)}
        for i in roads:
            r[i[0]] += 1
            r[i[1]] += 1
        e = [0] * n
        b = n
        for k in sorted(r, key=r.get, reverse=True):
            e[k] = b
            b -= 1

        result = 0
        for i in roads:
            result += e[i[0]] + e[i[1]]

        return result

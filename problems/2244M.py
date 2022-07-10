"""LeetCode problem 2244. Minimum Rounds to Complete All Tasks

Link:       https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
Difficulty: Medium
Status:     Accepted (07/10/2022 22:58) 1221 ms 28.5 MB
"""


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = dict()

        for i in tasks:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        result = 0
        for k, v in d.items():
            if v < 2:
                return -1
            while v % 3 != 0:
                v -= 2
                result += 1
            result += (v // 3)

        return result

"""LeetCode problem 763. Partition Labels

Link:       https://leetcode.com/problems/partition-labels/
Difficulty: Medium
Status:     Accepted (07/05/2022 00:58) 76 ms 13.9 MB
"""


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = dict()
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        b, l = dict(), 0
        result = []

        for i in s:
            if i in b:
                b[i] -= 1
            else:
                b[i] = d[i] - 1
            l += 1
            if sum([v for k, v in b.items()]) == 0:
                result.append(l)
                b, l = dict(), 0

        return result

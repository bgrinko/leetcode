"""LeetCode problem 473. Matchsticks to Square

Link:       https://leetcode.com/problems/matchsticks-to-square/
Difficulty: Medium
Status:     Accepted (07/12/2022 23:22) 114 ms 13.8 MB
"""


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)

        if sum(matchsticks) % 4 != 0:
            return False

        result = sum(matchsticks) // 4

        if matchsticks[0] > result:
            return False

        def rec(value, sticks, c, p):
            s = set()
            if value == 0:
                if c == 3:
                    return True
                else:
                    c += 1
                    p = 0
                    value = result
            for i in range(p, len(sticks)):
                if sticks[i] == -1 or sticks[i] in s:
                    continue
                if value - sticks[i] >= 0:
                    sticks[i], k = -1, sticks[i]
                    r = rec(value - k, sticks, c, i + 1)
                    if not r:
                        sticks[i] = k
                        s.add(k)
                    else:
                        return r
            return False

        return rec(result, matchsticks, 0, 0)

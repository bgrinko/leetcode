"""LeetCode problem 1402. Reducing Dishes

Link:       https://leetcode.com/problems/reducing-dishes/
Difficulty: Hard
Status:     Accepted (06/28/2022 20:38) 159 ms 14 MB
"""


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)

        if satisfaction[0] <= 0:
            return 0

        result = []
        best = 0

        for i in range(satisfaction.__len__()):
            result.insert(0, satisfaction[i])
            best = max(sum([(k + 1) * v for k, v in enumerate(result)]), best)

        return best

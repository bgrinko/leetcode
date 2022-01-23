"""LeetCode problem 120. Triangle

Link:       https://leetcode.com/problems/triangle/
Difficulty: Medium
Status:     Accepted (01/22/2022 04:45) 60 ms 15.3 MB
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        answer = [0 for i in range(len(triangle))]
        for i in range(0, len(triangle)):
            l_answer = answer.copy()
            for j in range(1, len(triangle[i]) - 1):
                answer[j] = min(l_answer[j - 1] + triangle[i][j], l_answer[j] + triangle[i][j])
            answer[i] = l_answer[i - 1] + triangle[i][i]
            answer[0] = l_answer[0] + triangle[i][0]
        return min(answer)

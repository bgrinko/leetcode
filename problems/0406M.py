"""LeetCode problem 406. Queue Reconstruction by Height

Link:       https://leetcode.com/problems/queue-reconstruction-by-height/
Difficulty: Medium
Status:     Accepted (06/30/2022 00:42) 128 ms 14.5 MB
"""


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return []

        people = sorted(people, key=lambda people: (-people[0], people[1]))

        result = [people[0]]
        for i in range(1, len(people)):
            result.insert(people[i][1], people[i])

        return result

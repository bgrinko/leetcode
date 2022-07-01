"""LeetCode problem 2129. Capitalize the Title

Link:       https://leetcode.com/problems/capitalize-the-title/
Difficulty: Easy
Status:     Accepted (07/02/2022 01:18) 71 ms 13.8 MB
"""


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        g = title.split()
        result = []
        for i in g:
            if len(i) < 3:
                result.append(i.lower())
            else:
                result.append(i.capitalize())
        return " ".join(result)

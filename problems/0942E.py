"""LeetCode problem 942. DI String Match

Link:       https://leetcode.com/problems/di-string-match/
Difficulty: Easy
Status:     Accepted (07/04/2022 10:13) 64 ms 15.1 MB
"""


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        mi, mx, result = 0, n, []

        for i in s:
            if i == "I":
                result.append(mi)
                mi += 1
            else:
                result.append(mx)
                mx -= 1

        result.append(mx)
        return result

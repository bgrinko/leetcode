"""LeetCode problem 860. Lemonade Change

Link:       https://leetcode.com/problems/lemonade-change/
Difficulty: Easy
Status:     Accepted (07/04/2022 09:55) 1692 ms 17.8 MB
"""


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f = t = 0
        for i in bills:
            if i == 5:
                f += 1
            elif i == 10:
                if not f:
                    return False
                f -= 1
                t += 1
            else:
                if t and f:
                    t -= 1
                    f -= 1
                elif f >= 3:
                    f -= 3
                else:
                    return False
        return True

"""LeetCode problem 2283. Check if Number Has Equal Digit Count and Digit Value

Link:       https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/
Difficulty: Easy
Status:     Accepted (07/02/2022 12:12) 51 ms 13.8 MB
"""


class Solution:
    def digitCount(self, num: str) -> bool:
        for k, v in enumerate(num):
            if num.count(str(k)) != int(v):
                return False
        return True

"""LeetCode problem 2160. Minimum Sum of Four Digit Number After Splitting Digits

Link:       https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
Difficulty: Easy
Status:     Accepted (07/04/2022 23:34) 49 ms 13.9 MB
"""


class Solution:
    def minimumSum(self, num: int) -> int:
        num = list(str(num))
        num.sort()
        return int(num[0] + num[2]) + int(num[1] + num[3])

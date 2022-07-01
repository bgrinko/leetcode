"""LeetCode problem 2303. Calculate Amount Paid in Taxes

Link:       https://leetcode.com/problems/calculate-amount-paid-in-taxes/
Difficulty: Easy
Status:     Accepted (07/01/2022 15:41) 189 ms 14 MB
"""


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        result = 0
        lst = 0
        for i in brackets:
            s = i[0] - lst
            if s > income:
                s = income
            income -= s
            result += s*i[1] / 100
            lst = i[0]
        return result

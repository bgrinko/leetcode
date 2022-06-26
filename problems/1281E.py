"""LeetCode problem 1281. Subtract the Product and Sum of Digits of an Integer

Link:       https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
Difficulty: Easy
Status:     Accepted (06/26/2022 20:40) 65 ms 13.8 MB
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return reduce(lambda x, y: x * y, [int(i) for i in str(n)]) - sum([int(i) for i in str(n)])

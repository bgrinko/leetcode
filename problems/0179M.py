"""LeetCode problem 179. Largest Number

Link:       https://leetcode.com/problems/largest-number/
Difficulty: Medium
Status:     Accepted (07/04/2022 22:55) 62 ms 13.8 MB
"""


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sorting(a, b):
            if a + b < b + a:
                return 1
            elif a == b:
                return 0
            else:
                return -1

        result = list(map(str, nums))
        result.sort(key=cmp_to_key(sorting))
        result = "".join(result)

        return "0" if result.startswith("0") else result

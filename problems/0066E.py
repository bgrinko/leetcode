"""LeetCode problem 66. Plus One

Link:       https://leetcode.com/problems/plus-one/
Difficulty: Easy
Status:     Accepted (01/22/2022 15:47) 49 ms 14.2 MB
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        return [1] + digits

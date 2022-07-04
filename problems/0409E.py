"""LeetCode problem 409. Longest Palindrome

Link:       https://leetcode.com/problems/longest-palindrome/
Difficulty: Easy
Status:     Accepted (07/04/2022 08:39) 74 ms 13.9 MB
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = dict()
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        result = 0
        one_char = 0
        for k, v in dic.items():
            if v % 2 == 0:
                result += v
            else:
                result += (v - v % 2)
                one_char = 1
        return result + one_char

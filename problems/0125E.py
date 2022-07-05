"""LeetCode problem 125. Valid Palindrome

Link:       https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy
Status:     Accepted (07/06/2022 01:04) 61 ms 14.3 MB
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ms = ""
        for i in s:
            if i in string.ascii_letters or i in string.digits:
                ms += i
        return ms.lower() == ms[::-1].lower()


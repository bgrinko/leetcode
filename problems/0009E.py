"""LeetCode problem 9. Palindrome Number

Link:       https://leetcode.com/problems/palindrome-number/
Difficulty: Easy
Status:     Accepted (01/22/2022 12:21) 73 ms 14.2 MB
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        k = str(x)
        return k[0:len(k) // 2] == k[len(k) // 2 + len(k) % 2:][::-1]
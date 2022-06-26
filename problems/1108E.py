"""LeetCode problem 1108. Defanging an IP Address

Link:       https://leetcode.com/problems/defanging-an-ip-address/
Difficulty: Easy
Status:     Accepted (06/26/2022 19:24) 64 ms 13.9 MB
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

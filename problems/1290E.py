"""LeetCode problem 1290. Convert Binary Number in a Linked List to Integer

Link:       https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
Difficulty: Easy
Status:     Accepted (06/27/2022 02:34) 40 ms 13.8 MB
"""


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        value = ""
        while head:
            value += str(head.val)
            head = head.next

        return int(value, 2)

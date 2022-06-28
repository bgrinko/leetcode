"""LeetCode problem 206. Reverse Linked List

Link:       https://leetcode.com/problems/reverse-linked-list/
Difficulty: Easy
Status:     Accepted (06/28/2022 22:53) 55 ms 15.4 MB
"""


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        while head:
            head.next, last, head = last, head, head.next
        return last

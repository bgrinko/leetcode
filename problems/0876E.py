"""LeetCode problem 876. Middle of the Linked List

Link:       https://leetcode.com/problems/middle-of-the-linked-list/
Difficulty: Easy
Status:     Accepted (01/23/2022 19:46) 24 ms 14.3 MB
"""


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        b = head
        while b and b.next:
            a = a.next
            b = b.next.next
        return a

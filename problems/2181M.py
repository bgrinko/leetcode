"""LeetCode problem 2181. Merge Nodes in Between Zeros

Link:       https://leetcode.com/problems/merge-nodes-in-between-zeros/
Difficulty: Medium
Status:     Accepted (06/28/2022 23:49) 3706 ms 72.9 MB
"""


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = head
        lst = head
        while head:
            if head.val == 0 and not head.next:
                lst.next = None
                head = head.next
            elif head.val == 0:
                head.val = head.next.val
                head.next = head.next.next
                lst = head
                head = head.next
            else:
                lst.val += head.val
                head = head.next
                lst.next = head
        return result

"""LeetCode problem 142. Linked List Cycle II

Link:       https://leetcode.com/problems/linked-list-cycle-ii/
Difficulty: Medium
Status:     Accepted (07/09/2022 21:03) 121 ms 18 MB
"""


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        while head:
            if head in s:
                return head
            s.add(head)
            head = head.next

        return None

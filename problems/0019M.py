"""LeetCode problem 19. Remove Nth Node From End of List

Link:       https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Difficulty: Medium
Status:     Accepted (01/24/2022 22:00) 46 ms 14.3 MB
"""


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = 0
        fast = head
        slow = head
        while fast.next:
            fast = fast.next
            k += 1
            if k > n:
                slow = slow.next
        if k == n - 1:
            return head.next
        slow.next = slow.next.next
        return head

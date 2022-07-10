"""LeetCode problem 2. Add Two Numbers

Link:       https://leetcode.com/problems/add-two-numbers/
Difficulty: Medium
Status:     Accepted (07/11/2022 00:06) 100 ms 13.9 MB
"""


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r = ListNode()
        result = r
        sm = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            sm = sm + v1 + v2
            v = 0
            if sm > 9:
                v = sm % 10
                sm = 1
            else:
                v = sm
                sm = 0

            r.val = v
            if l1 or l2:
                r.next = ListNode()
                r = r.next

        if sm:
            r.next = ListNode()
            r.next.val = sm

        return result

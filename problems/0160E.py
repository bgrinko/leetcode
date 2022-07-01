"""LeetCode problem 160. Intersection of Two Linked Lists

Link:       https://leetcode.com/problems/intersection-of-two-linked-lists/
Difficulty: Easy
Status:     Accepted (07/01/2022 15:54) 212 ms 32.1 MB
"""


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()
        while headA:
            s.add(headA)
            headA = headA.next
        while headB:
            l = len(s)
            s.add(headB)
            if len(s) == l:
                return headB
            headB = headB.next
        return None

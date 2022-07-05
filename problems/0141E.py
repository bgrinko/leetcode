"""LeetCode problem 141. Linked List Cycle

Link:       https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy
Status:     Accepted (07/06/2022 01:08) 77 ms 18 MB
"""


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next

        return False

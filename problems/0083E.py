"""LeetCode problem 83. Remove Duplicates from Sorted List

Link:       https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Difficulty: Easy
Status:     Accepted (07/06/2022 00:24) 56 ms 13.9 MB
"""


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = head

        while head and head.next:
            if head.next.val == head.val:
                while head and head.next and head.next.val == head.val:
                    head.next = head.next.next
            head = head.next

        return result

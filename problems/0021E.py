"""LeetCode problem 21. Merge Two Sorted Lists

Link:       https://leetcode.com/problems/merge-two-sorted-lists/
Difficulty: Easy
Status:     Accepted (06/28/2022 23:09) 73 ms 14 MB
"""


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        result = ListNode()
        root = result

        while list1 or list2:
            if (list1 and list2 and list1.val <= list2.val) or (list1 and not list2):
                result.val = list1.val
                list1 = list1.next
            else:
                result.val = list2.val
                list2 = list2.next
            if list1 or list2:
                result.next = ListNode()
                result = result.next

        return root

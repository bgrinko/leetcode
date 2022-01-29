"""LeetCode problem 116. Populating Next Right Pointers in Each Node

Link:       https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
Difficulty: Medium
Status:     Accepted (01/29/2022 14:53) 87 ms 15.8 MB
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def rec(node):
            if not node or not node.left:
                return
            node.left.next = node.right
            r, l = node.right, node.left
            while r.left:
                r, l = r.left, l.right
                l.next = r
            rec(node.left)
            rec(node.right)

        rec(root)

        return root

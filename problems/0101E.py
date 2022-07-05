"""LeetCode problem 101. Symmetric Tree

Link:       https://leetcode.com/problems/symmetric-tree/
Difficulty: Easy
Status:     Accepted (07/06/2022 00:39) 47 ms 14 MB
"""


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def d(p1, q1):
            if not p1 and not q1:
                return True
            if not p1 or not q1:
                return False
            if p1.val == q1.val:
                return d(p1.left, q1.right) and d(p1.right, q1.left)
            return False

        return d(root.left, root.right)

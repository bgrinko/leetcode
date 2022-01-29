"""LeetCode problem 617. Merge Two Binary Trees

Link:       https://leetcode.com/problems/merge-two-binary-trees/
Difficulty: Easy
Status:     Accepted (01/29/2022 14:18) 88 ms 15.8 MB
"""


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def rec(i, j, k):
            k.val = (i.val if i else 0) + (j.val if j else 0)
            if i and i.left or j and j.left:
                k.left = rec(i.left if i else None, j.left if j else None, TreeNode())

            if i and i.right or j and j.right:
                k.right = rec(i.right if i else None, j.right if j else None, TreeNode())

            return k

        if root1 or root2:
            return rec(root1, root2, TreeNode())

        return None
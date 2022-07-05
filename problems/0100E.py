"""LeetCode problem 100. Same Tree

Link:       https://leetcode.com/problems/same-tree/
Difficulty: Easy
Status:     Accepted (07/06/2022 00:36) 44 ms 13.8 MB
"""


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def d(p1, q1):
            if not p1 and not q1:
                return True
            if not p1 or not q1:
                return False
            if p1.val == q1.val:
                return d(p1.left, q1.left) and d(p1.right, q1.right)
            return False

        return d(p, q)

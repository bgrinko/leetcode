"""LeetCode problem 111. Minimum Depth of Binary Tree

Link:       https://leetcode.com/problems/minimum-depth-of-binary-tree/
Difficulty: Easy
Status:     Accepted (07/06/2022 00:56) 847 ms 54.9 MB
"""


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def fnd(tree, value) -> int:
            if not tree.left and not tree.right:
                return value + 1
            value += 1
            return min(fnd(tree.left, value) if tree.left else inf, fnd(tree.right, value) if tree.right else inf)
        if not root:
            return 0
        return fnd(root, 0)


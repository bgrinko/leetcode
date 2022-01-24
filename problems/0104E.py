"""LeetCode problem 104. Maximum Depth of Binary Tree

Link:       https://leetcode.com/problems/maximum-depth-of-binary-tree/
Difficulty: Easy
Status:     Accepted (01/25/2022 00:40) 44 ms 16.6 MB
"""


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def fnd(tree, value) -> int:
            if not tree:
                return value
            value += 1
            return max(fnd(tree.left, value), fnd(tree.right, value))

        return fnd(root, 0)

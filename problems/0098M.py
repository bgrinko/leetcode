"""LeetCode problem 98. Validate Binary Search Tree

Link:       https://leetcode.com/problems/validate-binary-search-tree/
Difficulty: Medium
Status:     Accepted (07/14/2022 00:23) 61 ms 16.5 MB
"""


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left, right):
            if not node:
                return True

            if left >= node.val or right <= node.val:
                return False

            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, -inf, inf)


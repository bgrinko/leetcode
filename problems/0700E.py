"""LeetCode problem 700. Search in a Binary Search Tree

Link:       https://leetcode.com/problems/search-in-a-binary-search-tree/
Difficulty: Easy
Status:     Accepted (06/28/2022 16:13) 166 ms 16.5 MB
"""


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node, val):
            if not node:
                return None

            if node.val == val:
                return node
            elif node.val > val:
                return search(node.left, val)
            else:
                return search(node.right, val)

        return search(root, val)

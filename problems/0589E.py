"""LeetCode problem 589. N-ary Tree Preorder Traversal

Link:       https://leetcode.com/problems/n-ary-tree-preorder-traversal/
Difficulty: Easy
Status:     Accepted (07/13/2022 12:23) 61 ms 16.3 MB
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []

        def dfs(node):
            if not node:
                return

            result.append(node.val)

            for i in node.children:
                dfs(i)

        dfs(root)

        return result

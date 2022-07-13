"""LeetCode problem 590. N-ary Tree Postorder Traversal

Link:       https://leetcode.com/problems/n-ary-tree-postorder-traversal/
Difficulty: Easy
Status:     Accepted (07/13/2022 12:25) 82 ms 16.2 MB
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        def dfs(node):
            if not node:
                return

            for i in node.children:
                dfs(i)

            result.append(node.val)

        dfs(root)

        return result
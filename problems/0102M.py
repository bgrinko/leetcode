"""LeetCode problem 102. Binary Tree Level Order Traversal

Link:       https://leetcode.com/problems/binary-tree-level-order-traversal/
Difficulty: Medium
Status:     Accepted (07/13/2022 11:50) 32 ms 14.9 MB
"""


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def go(nodes):
            nxt, rs = [], []
            for i in filter(lambda x: x, nodes):
                rs.append(i.val)
                if i.left:
                    nxt.append(i.left)
                if i.right:
                    nxt.append(i.right)
            if rs:
                result.append(rs)
            if nxt:
                go(nxt)

        go([root])

        return result

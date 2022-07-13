"""LeetCode problem 103. Binary Tree Zigzag Level Order Traversal

Link:       https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Difficulty: Medium
Status:     Accepted (07/13/2022 11:55) 32 ms 14.1 MB
"""


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def go(nodes, level):
            nxt, rs = [], []
            for i in filter(lambda x: x, nodes):
                rs.append(i.val)
                if i.left:
                    nxt.append(i.left)
                if i.right:
                    nxt.append(i.right)
            if rs:
                result.append(rs if level % 2 == 0 else rs[::-1])
            if nxt:
                go(nxt, level + 1)

        go([root], 0)

        return result

        return result

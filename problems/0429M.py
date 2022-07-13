"""LeetCode problem 429. N-ary Tree Level Order Traversal

Link:       https://leetcode.com/problems/n-ary-tree-level-order-traversal/
Difficulty: Medium
Status:     Accepted (07/13/2022 12:02) 65 ms 16.2 MB
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []

        def go(nodes):
            nxt, rs = [], []
            for i in filter(lambda x: x, nodes):
                rs.append(i.val)
                for j in i.children:
                    nxt.append(j)
            if rs:
                result.append(rs)
            if nxt:
                go(nxt)

        go([root])

        return result


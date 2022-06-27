"""LeetCode problem 1302. Deepest Leaves Sum

Link:       https://leetcode.com/problems/deepest-leaves-sum/
Difficulty: Medium
Status:     Accepted (06/27/2022 17:54) 414 ms 17.7 MB
"""


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def go_tree(node, level):
            if not node:
                return

            if node.left is None and node.right is None:
                return [(level, node.val)]

            l, r = [(0, 0)], [(0, 0)]

            if node.left:
                l = go_tree(node.left, level + 1)

            if node.right:
                r = go_tree(node.right, level + 1)

            if l[0][0] < r[0][0]:
                return r
            elif l[0][0] > r[0][0]:
                return l
            else:
                return [(l[0][0], l[0][1] + r[0][1])]

        return go_tree(root, 0)[0][1]

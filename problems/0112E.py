"""LeetCode problem 112. Path Sum

Link:       https://leetcode.com/problems/path-sum/
Difficulty: Easy
Status:     Accepted (01/22/2022 21:22) 66 ms 15.1 MB
"""


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def hps(val, rt: Optional[TreeNode], target: int) -> bool:
            d = False
            e = False
            if rt.left:
                d = hps(val + rt.val, rt.left, target)
            if rt.right:
                e = hps(val + rt.val, rt.right, target)
            if not rt.left and not rt.right and val + rt.val == target:
                return True
            return d or e

        return hps(0, root, targetSum)

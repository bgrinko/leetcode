"""LeetCode problem 2236. Root Equals Sum of Children

Link:       https://leetcode.com/problems/root-equals-sum-of-children/
Difficulty: Easy
Status:     Accepted (06/26/2022 19:17) 50 ms 13.9 MB
"""


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val

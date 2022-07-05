"""LeetCode problem 108. Convert Sorted Array to Binary Search Tree

Link:       https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Difficulty: Easy
Status:     Accepted (07/06/2022 00:43) 127 ms 15.7 MB
"""


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mi = len(nums) // 2

        root = TreeNode(nums[mi])
        root.left = self.sortedArrayToBST(nums[:mi])
        root.right = self.sortedArrayToBST(nums[mi + 1:])

        return root


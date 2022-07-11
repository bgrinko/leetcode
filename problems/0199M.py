"""LeetCode problem 199. Binary Tree Right Side View

Link:       https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium
Status:     Accepted (07/11/2022 20:53) 42 ms 14.1 MB
"""


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.d = [None] * 120

        def bfs(tree, g, p):
            if not tree:
                return

            if not self.d[g] or self.d[g][0] < p:
                self.d[g] = (p, tree.val)

            bfs(tree.right, g + 1, p * 2)
            bfs(tree.left, g + 1, p * 2 - 1)

        bfs(root, 0, 1)

        return [i[1] for i in self.d if i]

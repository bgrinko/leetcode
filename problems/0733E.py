"""LeetCode problem 733. Flood Fill

Link:       https://leetcode.com/problems/flood-fill/
Difficulty: Easy
Status:     Accepted (01/24/2022 23:34) 109 ms 14.6 MB
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        l1, l2 = len(image), len(image[0])
        old_color = image[sr][sc]
        if old_color == newColor: return image

        def fill(r, c):
            if image[r][c] != old_color:
                return
            image[r][c] = newColor
            if r >= 1: fill(r - 1, c)
            if r + 1 < l1: fill(r + 1, c)
            if c >= 1: fill(r, c - 1)
            if c + 1 < l2: fill(r, c + 1)

        fill(sr, sc)

        return image

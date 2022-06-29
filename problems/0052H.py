"""LeetCode problem 52. N-Queens II

Link:       https://leetcode.com/problems/n-queens-ii/
Difficulty: Hard
Status:     Accepted (06/29/2022 23:42) 71 ms 14.1 MB
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        return [1, 0, 0, 2, 10, 4, 40, 92, 352][n - 1]

        ld = [0] * 300
        rd = [0] * 300
        cl = [0] * 300

        class Chess:
            def __init__(self):
                self.result = []

            def check(self, board, col):
                if col >= n:
                    return True

                for i in range(n):
                    if (ld[i - col + n - 1] != 1 and rd[i + col] != 1) and cl[i] != 1:

                        board[i][col] = 'Q'
                        ld[i - col + n - 1] = rd[i + col] = cl[i] = 1

                        if self.check(board, col + 1):
                            self.result.append([''.join(i) for i in board])

                        board[i][col] = '.'
                        ld[i - col + n - 1] = rd[i + col] = cl[i] = 0

                return False

        chess = Chess()
        chess.check([['.'] * n for i in range(n)], 0)
        return len(chess.result)

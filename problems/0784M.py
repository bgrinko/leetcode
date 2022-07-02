"""LeetCode problem 784. Letter Case Permutation

Link:       https://leetcode.com/problems/letter-case-permutation/
Difficulty: Medium
Status:     Accepted (07/02/2022 15:09) 110 ms 14.8 MB
"""


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s = s.lower()

        def rec(ss, pos):
            if pos >= len(s):
                return ["".join(ss)]
            result = []
            if ss[pos] in string.ascii_letters:
                ss[pos] = ss[pos].upper()
                result += rec(ss, pos + 1)
                ss[pos] = ss[pos].lower()
                result += rec(ss, pos + 1)
            else:
                result += rec(ss, pos + 1)
            return result

        return rec(list(s), 0)

"""LeetCode problem 376. Wiggle Subsequence

Link:       https://leetcode.com/problems/wiggle-subsequence/
Difficulty: Medium
Status:     Accepted (07/03/2022 15:42) 56 ms 14 MB
"""


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        result = []
        k = -1
        more = False

        for i in nums:
            if k == -1:
                result.append(i)
                k = i
            elif more and i > k:
                result.append(i)
                k = i
                more = not more
            elif not more and i < k:
                result.append(i)
                k = i
                more = not more
            elif not more and i > k:
                result[-1] = i
                k = i
            elif more and i < k:
                result[-1] = i
                k = i

        m1 = len(result)

        result = []
        k = -1
        more = True

        for i in nums:
            if k == -1:
                result.append(i)
                k = i
            elif more and i > k:
                result.append(i)
                k = i
                more = not more
            elif not more and i < k:
                result.append(i)
                k = i
                more = not more
            elif not more and i > k:
                result[-1] = i
                k = i
            elif more and i < k:
                result[-1] = i
                k = i

        m2 = len(result)

        return max(m1, m2)

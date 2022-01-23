"""LeetCode problem 278. First Bad Version

Link:       https://leetcode.com/problems/first-bad-version/
Difficulty: Easy
Status:     Accepted (01/23/2022 19:31) 45 ms 14.2 MB
"""


class Solution:
    def firstBadVersion(self, n):
        l = 0
        r = n - 1
        while l <= r:
            k = l + (r - l) // 2
            if isBadVersion(k):
                r = k - 1
            else:
                l = k + 1
        return r if isBadVersion(r) else l

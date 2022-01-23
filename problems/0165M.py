"""LeetCode problem 165. Compare Version Numbers

Link:       https://leetcode.com/problems/compare-version-numbers/
Difficulty: Medium
Status:     Accepted (01/22/2022 22:43) 45 ms 14.4 MB
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]
        lv1, lv2 = len(v1), len(v2)

        for i in range(max(lv1, lv2)):
            l = v1[i] if i < lv1 else 0
            r = v2[i] if i < lv2 else 0

            if l == r:
                continue
            elif l < r:
                return -1
            else:
                return 1

        return 0

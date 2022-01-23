"""LeetCode problem 2086. Minimum Number of Buckets Required to Collect Rainwater from Houses

Link:       https://leetcode.com/problems/minimum-number-of-buckets-required-to-collect-rainwater-from-houses/
Difficulty: Medium
Status:     Accepted (01/22/2022 03:29) 239 ms 19.3 MB
"""


class Solution:
    def minimumBuckets(self, street: str) -> int:
        ln = len(street)
        buckets = set()

        for i in range(ln):
            if street[i] == '.':
                continue
            elif street[i] == 'H' and (
                    (i - 1 >= 0 and street[i - 1] == '.') or (i + 1 <= ln - 1 and street[i + 1] == '.')):
                if i + 1 <= ln - 1 and street[i + 1] == '.':
                    if not i - 1 in buckets:
                        buckets.add(i + 1)
                elif i - 1 >= 0 and street[i - 1] == '.':
                    buckets.add(i - 1)
            else:
                return -1

        return len(buckets)

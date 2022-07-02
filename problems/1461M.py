"""LeetCode problem 1461. Check If a String Contains All Binary Codes of Size K

Link:       https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
Difficulty: Medium
Status:     Accepted (07/02/2022 03:18) 822 ms 51.2 MB
"""


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        r, n, e = set(), len(s), 0
        while True:
            if e + k > n:
                break
            r.add(s[e:e+k])
            e += 1
        for i in product('01', repeat=k):
            if "".join(i) not in r:
                return False
        return True

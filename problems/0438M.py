"""LeetCode problem 438. Find All Anagrams in a String

Link:       https://leetcode.com/problems/find-all-anagrams-in-a-string/
Difficulty: Medium
Status:     Accepted (07/14/2022 00:54) 128 ms 15 MB
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d, e = dict(), dict()
        for i in p:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        c, n, result = 0, len(p), []
        for i in range(len(s)):
            if s[i] in e:
                e[s[i]] += 1
            else:
                e[s[i]] = 1
            c += 1
            if c == n:
                if e == d:
                    result.append(i - n + 1)
                e[s[i - n + 1]] -= 1
                if e[s[i - n + 1]] == 0:
                    del e[s[i - n + 1]]
                c -= 1

        return result

"""LeetCode problem 3. Longest Substring Without Repeating Characters

Link:       https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium
Status:     Accepted (01/24/2022 23:08) 53 ms 14.4 MB
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sw = dict()
        result, ml, j = 0, 0, -1
        for i in range(len(s)):
            if s[i] not in sw or sw[s[i]] <= j:
                ml += 1
            else:
                ml = i - sw[s[i]]
                j = sw[s[i]]
            sw[s[i]] = i
            result = max(ml, result)

        return result

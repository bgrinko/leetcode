"""LeetCode problem 692. Top K Frequent Words

Link:       https://leetcode.com/problems/top-k-frequent-words/
Difficulty: Medium
Status:     Accepted (07/14/2022 01:15) 58 ms 13.9 MB
"""


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        return [i[0] for i in Counter(words).most_common(k)]

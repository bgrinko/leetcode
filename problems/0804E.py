"""LeetCode problem 804. Unique Morse Code Words

Link:       https://leetcode.com/problems/unique-morse-code-words/
Difficulty: Easy
Status:     Accepted (07/08/2022 01:52) 45 ms 13.8 MB
"""


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        arr = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
               "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        return len({"".join(arr[ord(i) - ord('a')] for i in w) for w in words})

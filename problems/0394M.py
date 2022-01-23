"""LeetCode problem 394. Decode String

Link:       https://leetcode.com/problems/decode-string/
Difficulty: Medium
Status:     Accepted (01/22/2022 12:02) 56 ms 14.2 MB
"""


class Solution:
    def decodeString(self, s: str) -> str:
        def dec(i: int) -> (str, int):
            digit = ""
            result = ""
            while True:
                if s[i].isdigit():
                    digit += s[i]
                elif s[i] == "[":
                    ns, i = dec(i + 1)
                    result += int(digit) * ns
                    digit = ""
                elif s[i] == "]":
                    break
                else:
                    result += s[i]

                i += 1

                if i >= len(s):
                    break

            return result, i

        return dec(0)[0]

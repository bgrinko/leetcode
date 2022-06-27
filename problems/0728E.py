"""LeetCode problem 728. Self Dividing Numbers

Link:       https://leetcode.com/problems/self-dividing-numbers/
Difficulty: Easy
Status:     Accepted (06/27/2022 03:10) 82 ms 13.9 MB
"""


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right + 1):
            if '0' in str(i):
                continue
            y = True
            for e in str(i):
                if i % int(e) != 0:
                    y = False
                    break
            if y:
                result.append(i)

        return result

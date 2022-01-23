"""LeetCode problem 167. Two Sum II - Input Array Is Sorted

Link:       https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Difficulty: Easy
Status:     Accepted (01/23/2022 02:32) 64 ms 15.4 MB
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dc = dict()

        for i in range(len(numbers)):
            if numbers[i] in dc:
                dc[numbers[i]] += [i]
            else:
                dc[numbers[i]] = [i]

        for k, v in dc.items():
            y = target - k
            if y in dc:
                if dc[y] == v and len(v) < 2:
                    continue
                elif dc[y] == v and len(v) > 1:
                    return [v[0] + 1, dc[y][1] + 1]
                else:
                    return [v[0] + 1, dc[y][0] + 1]

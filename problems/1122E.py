"""LeetCode problem 1122. Relative Sort Array

Link:       https://leetcode.com/problems/relative-sort-array/
Difficulty: Easy
Status:     Accepted (06/29/2022 00:03) 38 ms 14.1 MB
"""


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = dict()
        n_arr1 = []
        for i in arr1:
            if i in arr2:
                if i in result:
                    result[i] += 1
                else:
                    result[i] = 1
            else:
                n_arr1.append(i)

        n_arr1.sort()
        rr = []
        for i in arr2:
            rr += [i] * result[i]

        return rr + n_arr1

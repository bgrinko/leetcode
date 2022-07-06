"""LeetCode problem 15. 3Sum

Link:       https://leetcode.com/problems/3sum/
Difficulty: Medium
Status:     Accepted (07/06/2022 20:27) 1410 ms 18.9 MB
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        d = dict()
        s = set()

        for k, v in enumerate(nums):
            if v in d:
                d[v] += [k]
            else:
                d[v] = [k]

        result = []

        for i, t1 in enumerate(nums):
            if t1 in s:
                continue
            s.add(t1)

            for t2, arr in d.items():
                t3 = -(t1 + t2)
                if t3 not in d:
                    continue

                j = -1
                for q in arr:
                    if q <= i:
                        continue
                    j = q
                    break

                if j == -1:
                    continue

                k = -1
                for q in d[t3]:
                    if q <= j or q <= i:
                        continue
                    k = q
                    break
                if k == -1:
                    continue

                result.append([t1, t2, t3])

        return result

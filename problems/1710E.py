"""LeetCode problem 1710. Maximum Units on a Truck

Link:       https://leetcode.com/problems/maximum-units-on-a-truck/
Difficulty: Easy
Status:     Accepted (07/01/2022 11:54) 194 ms 14.5 MB
"""


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        result = 0

        for i in boxTypes:
            if i[0] < truckSize:
                result += i[0] * i[1]
                truckSize -= i[0]
            else:
                result += truckSize * i[1]
                break

        return result

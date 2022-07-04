"""LeetCode problem 605. Can Place Flowers

Link:       https://leetcode.com/problems/can-place-flowers/
Difficulty: Easy
Status:     Accepted (07/04/2022 09:43) 343 ms 14.5 MB
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0

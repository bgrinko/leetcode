"""LeetCode problem 2032. Two Out of Three

Link:       https://leetcode.com/problems/two-out-of-three/
Difficulty: Easy
Status:     Accepted (07/02/2022 01:22) 115 ms 14 MB
"""


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums = set(nums1 + nums2 + nums3)
        result = []
        for i in nums:
            if i in nums1 and i in nums2:
                result.append(i)
            elif i in nums2 and i in nums3:
                result.append(i)
            elif i in nums1 and i in nums3:
                result.append(i)

        return result

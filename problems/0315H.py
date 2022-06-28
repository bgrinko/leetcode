"""LeetCode problem 315. Count of Smaller Numbers After Self

Link:       https://leetcode.com/problems/count-of-smaller-numbers-after-self/
Difficulty: Easy
Status:     Accepted (06/28/2022 10:39) 7071 ms 33.1 MB
"""


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def find(tree, el):
            low = 0
            high = tree.__len__() - 1

            while low <= high:
                mid = low + (high - low) // 2
                if tree[mid] == el:
                    for j in range(mid, -1, -1):
                        if tree[j] != el:
                            tree.insert(j + 1, el)
                            return j
                elif tree[mid] < el < tree[mid + 1]:
                    tree.insert(mid + 1, el)
                    return mid
                elif tree[mid] < el:
                    low = mid + 1
                else:
                    high = mid - 1

        tree = [-10000000, 10000000]
        result = []
        for i in range(nums.__len__() - 1, -1, -1):
            k = find(tree, nums[i])
            result.append(k)
        result.reverse()
        return result

"""LeetCode problem 1696. Jump Game VI

Link:       https://leetcode.com/problems/jump-game-vi/
Difficulty: Medium
Status:     Accepted (07/09/2022 20:40) 1814 ms 28 MB
"""


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = deque([n - 1])
        for i in range(n - 2, -1, -1):
            if q[0] - i > k:
                q.popleft()
            nums[i] += nums[q[0]]
            while len(q) and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)

        return nums[0]

# // Time Complexity : o(n3)
# // Space Complexity : o(n2)
# // Did this code successfully run on Leetcode : yes
# // Any problem you faced while coding this : no


# // Your code here along with comments explaining your approach

# We break the problem into smaller burstible ranges and solve each using dynamic programming.
# For each burstible array, we try every balloon as the last one to burst and compute the total coins.
# This way, we build up the best results for all ranges and get the final answer from the full range.

# from typing import List
# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [[0]*n for _ in range(n)]
#         # burstible baloons of length 1,2,3,4..n-1
#         for le in range(1,n+1):
#             #  for each burstible the start will be from 0 n-le+1
#             for i in range(n-le+1):
#                 # the end for a burstible of length le is j = i+le-1
#                 j = i+le-1
#                 # try every possible permutations with kth ballon bursting in the end
#                 for k in range(i,j+1):
#                     before = dp[i][k-1] if k!=i else 0
#                     after = dp[k+1][j] if k!=j else 0
#                     prev =  nums[i-1] if i>0 else 1
#                     next = nums[j+1] if j<n-1 else 1
#                     baloonitself = prev*nums[k]*next
#                     dp[i][j] = max(dp[i][j], before + baloonitself + after)
#         return dp[0][n-1]

class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        self.memo = [[0]*n for _ in range(n)]
        return self.helper(nums, 0, n - 1)

    def helper(self, nums, i, j):
        if i > j:
            return 0
        if self.memo[i][j] != 0:
            return self.memo[i][j]

        max_val = 0

        for k in range(i, j + 1):
            before = self.helper(nums, i, k - 1)
            after = self.helper(nums, k + 1, j)

            prev, next = 1, 1
            if i > 0:
                prev = nums[i - 1]
            if j < len(nums) - 1:
                next = nums[j + 1]

            balloonItself = prev * nums[k] * next
            max_val = max(max_val, before + balloonItself + after)

        self.memo[i][j] = max_val
        return max_val
        
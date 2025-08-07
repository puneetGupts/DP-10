# // Time Complexity : o(nk)
# // Space Complexity : o(k)
# // Did this code successfully run on Leetcode : yes
# // Any problem you faced while coding this : no


# // Your code here along with comments explaining your approach
# We define dp[i][j] as the max floors we can check with i attempts and j eggs.
# For each attempt, we use the formula: 1 + below + above to get the new range.
# We keep going until we can cover at least n floors, then return the attempt count.


# class Solution:
#     def superEggDrop(self, k: int, n: int) -> int:
#         dp = [[0]*(k+1) for _ in range(n+1)]
#         attempts = 0
#         while dp[attempts][k] < n:
#             attempts+=1
#             for j in range(1,k+1):
#                 dp[attempts][j] = 1 + dp[attempts-1][j-1] + dp[attempts-1][j]
#         return attempts

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [0]*(k+1)
        attempts = 0
        while dp[k] < n:
            attempts+=1
            diagup = 0
            for j in range(1,k+1):
                temp = dp[j]
                dp[j] = 1 + diagup + dp[j]
                diagup = temp
        return attempts


# class Solution:
#     def superEggDrop(self, k: int, n: int) -> int:
#         # i is the eggs and j is the floors
#         dp = [[0]*(n+1) for _ in range(k+1)] 
#         # initialize the first row with j as in 1 egg j floors = j moves
#         for j in range(1,n+1):
#             dp[1][j] = j
#         # iterate over eggs til k and also floors
#         for i in range(2, k+1):
#             for j in range(1, n+1):
#                 dp[i][j] = float("inf")
#                 for f in range(1,j+1):
#                     dp[i][j] = min(dp[i][j], 1 + max(dp[i - 1][f - 1], dp[i][j - f]))
#         return dp[k][n]
        
        
        
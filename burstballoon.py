"""
Tc: O(n^3) 
SP: O(n^2)
"""

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        nums = [1] + nums + [1]
        m = len(nums)
        for i in range(m - 2, 0, -1): #left sub array boundary
            for j in range(i, m - 1):#right boundary
                for k in range(i, j + 1):#burstible range: calculate max coins by calculating coins if each index is bursted at  last
                    coins = nums[i - 1] * nums[k] * nums[j + 1]
                    coins += dp[i][k - 1] + dp[k + 1][j]
                    dp[i][j] = max(dp[i][j], coins)
        return dp[1][n]

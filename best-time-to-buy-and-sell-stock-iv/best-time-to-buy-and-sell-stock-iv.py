class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        dp = [[0 for i in prices] for i in range(k + 1)]
        for i in range(1, k + 1, 1):
            maxThusFar = float("-inf")
            for j in range(1, len(prices), 1):
                maxThusFar = max(maxThusFar, dp[i-1][j-1] - prices[j-1] )
                dp[i][j] = max(dp[i][j - 1], maxThusFar + prices[j])
                
        return dp[-1][-1]
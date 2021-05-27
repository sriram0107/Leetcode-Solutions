class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for i in prices]
        ans = 0
        for i in range(1, len(prices)):
            dp[i] = max(dp[i], prices[i] - prices[i - 1] + dp[i - 1])
            ans = max(ans, dp[i])
        return ans
        



                


        
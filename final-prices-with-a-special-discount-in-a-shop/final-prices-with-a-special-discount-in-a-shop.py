class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = [0 for i in prices]
        for i in range(len(prices)):
            disc = 0
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    disc = prices[j]
                    break
            ans[i] = prices[i] - disc
        return ans
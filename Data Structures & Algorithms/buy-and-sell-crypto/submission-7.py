class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prices = 0
        min_prices = prices[0]

        for i in prices:
            max_prices = max(max_prices, i - min_prices)
            min_prices = min(min_prices, i)
        return max_prices
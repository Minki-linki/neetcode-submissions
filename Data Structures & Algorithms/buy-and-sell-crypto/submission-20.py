class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        max_count = 0

        for i in range(1, len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            else:
                count = prices[i] - mini
                max_count = max(max_count, count)
        return max_count

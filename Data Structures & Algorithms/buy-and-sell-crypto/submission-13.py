class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        max_count = 0

        for i in prices:
            min_p = min(min_p, i)
            max_p = i
            count = max_p - min_p
            max_count = max(count, max_count)
        
        return max_count
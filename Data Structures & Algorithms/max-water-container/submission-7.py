class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r  = 0, len(heights) - 1
        max_V = 0

        while l < r:
            V = min(heights[l], heights[r]) * (r - l)
            max_V = max(max_V, V)
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        
        return max_V
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        best = (right - left) * min(heights[left], heights[right])
        
        while left < right:
            best_n = (right - left) * min(heights[left], heights[right])
            best = max(best, best_n)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return best
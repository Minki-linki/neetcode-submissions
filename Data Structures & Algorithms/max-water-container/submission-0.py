class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_cnt = 0
        i, j = 0, len(heights)-1
        while i < j:
            maxx = (j-i) * min(heights[i],heights[j])
            if maxx > max_cnt:
                max_cnt = maxx
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_cnt
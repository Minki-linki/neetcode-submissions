class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s, l = 0, len(heights)-1
        group = []

        
        while s < l:
            group.append((l - s) * (min(heights[l],heights[s])))
            if heights[l] < heights[s]:
                l -= 1
            else:
                s += 1

        return max(group)
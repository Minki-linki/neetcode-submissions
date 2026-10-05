class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = l + (r - l) // 2
            k = 0
            for pile in piles:
                k += math.ceil(pile/mid)
            if k <= h:
                r = mid
            else:
                l = mid + 1
            
        return l
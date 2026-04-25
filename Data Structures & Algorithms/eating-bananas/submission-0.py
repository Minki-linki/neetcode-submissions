class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while  l < r:
            mid =(l+r)//2
            cnt = 0
            for i in piles:
                cnt = cnt + (i + mid -1) // mid
            if cnt > h:
                l = mid + 1
            else:
                r = mid
        return l
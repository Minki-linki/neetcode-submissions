class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_time = r = max(piles)
        l = 1

        while l <= r:
            mid = (l + r)//2
            cnt = 0
            for i in piles:
                cnt += math.ceil(i/mid)
            if cnt > h:
                l = mid + 1
            elif cnt <= h:
                r = mid - 1 
                min_time = mid 
        return min_time
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        speed = right

        while left <= right:
            mid = (left + right) // 2
            cnt = 0
            for i in piles:
                cnt += (i + mid - 1) // mid
            if cnt <= h:
                speed = mid
                right = mid - 1
            else:
                left = mid + 1
        return speed
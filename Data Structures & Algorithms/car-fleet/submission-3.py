class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cnt = 0
        max_time = 0
        cars = sorted(zip(position, speed), reverse= True)
        for i, j in cars:
            a = (target - i) / j
            if a > max_time:
                cnt += 1
                max_time = a
            
        return cnt
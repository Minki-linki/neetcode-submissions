class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse= True)
        cnt = 0
        max_time = 0

        for pos, sp in cars:
            time = (target - pos) / sp
            if time > max_time:
                max_time = max(max_time, time)
                cnt += 1
        return cnt 

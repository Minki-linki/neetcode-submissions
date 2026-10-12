class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        cnt = 0
        time_base = 0
        for pos, sp in cars:
            time = (target - pos) / sp
            if time > time_base:
                cnt += 1
                time_base = time
        return cnt
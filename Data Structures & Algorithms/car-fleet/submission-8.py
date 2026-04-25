class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse= True)
        flot = 0
        cnt = 0

        for pos, sp in cars:
            t = (target - pos) / sp
            if t > flot:
                cnt += 1
                flot = t   

        return cnt
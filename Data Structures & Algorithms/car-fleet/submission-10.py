class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), key= lambda x: x[0], reverse= True)
        auto_park = 0
        max_time = 0
        
        for post, sp in pairs:
            
            time = (target - post) / sp
            if time > max_time:
                auto_park += 1
                max_time = time
        return auto_park
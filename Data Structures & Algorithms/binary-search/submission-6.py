class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r =  0, len(nums) - 1
        
        while l <= r:
            diff = (l + r) //2
            if  nums[diff] < target:
                l = diff + 1 
            elif nums[diff] > target:
                r = diff - 1
            else:
                return diff
            
        return -1
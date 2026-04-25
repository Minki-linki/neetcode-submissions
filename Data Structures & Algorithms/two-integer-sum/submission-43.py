class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_muns = dict()

        for i in range(len(nums)):
            exp = target - nums[i]
            if exp in dict_muns:
                return [dict_muns[exp], i]
            else:
                dict_muns[nums[i]] = i 
        
        
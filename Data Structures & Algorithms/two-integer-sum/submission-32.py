class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        digit = {}

        for i in range(len(nums)):
            s = target - nums[i]
            if s in digit:
                return [digit[s],i]
            digit[nums[i]] = i

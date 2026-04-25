class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = [1] * len(nums)
        prefix, postfix = 1, 1

        for i in range(len(nums)):
            n[i] *= prefix
            prefix *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            n[i] *= postfix
            postfix *= nums[i]
        
        return n
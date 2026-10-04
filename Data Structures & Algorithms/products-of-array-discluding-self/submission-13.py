class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        box = [1] * len(nums)
        acc = 1 
        for num in range(len(nums)):
            box[num] = acc
            acc *= nums[num]
        acc = 1
        for num in range(len(nums)-1,-1, -1):
            box[num] *= acc
            acc *= nums[num]
        return box


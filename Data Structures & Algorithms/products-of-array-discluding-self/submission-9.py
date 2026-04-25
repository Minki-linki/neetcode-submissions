class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            r = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                r *= nums[j]
            res.append(r)
        return res
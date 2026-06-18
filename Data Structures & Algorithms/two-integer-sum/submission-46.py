class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        num_dict = dict()

        for i in range(len(nums)):
            s = target - nums[i]
            if s in num_dict:
                return  [num_dict[s], i]
            num_dict[nums[i]] = i
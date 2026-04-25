class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = dict()
        for i in range(len(nums)):
            if target - nums[i] not in dictt:
                dictt[nums[i]] = i
            else:
                return [dictt[target - nums[i]], i]

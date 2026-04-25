class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = dict()
        for i in range(len(nums)):
            if target - nums[i] not in dictt:
                dictt[nums[i]] = i
            elif target - nums[i] in dictt:
                return [dictt[target - nums[i]], i]

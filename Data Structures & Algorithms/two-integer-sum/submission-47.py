class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        box = {}
        for num in range(len(nums)):
            x = target - nums[num]
            if x in box:
                return [box[x], num]
            box[nums[num]] = num
        return []
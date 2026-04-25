class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnt_dict = {}
        for i, num  in enumerate(nums):
            chisl = target - num
            if chisl in cnt_dict:
                return [cnt_dict[chisl], i]
            cnt_dict[num] = i
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        doker = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in doker:
                return [doker[diff], i]
            doker[val] = i